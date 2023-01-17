from sqlalchemy import create_engine, insert, select, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import pyodbc
import pandas as pd
from scrapfun import get_html, get_container_pack, check_new_url, get_ingredients, unit_word_mapper, ingredient_map, num_amount, breakup_ingredients
from localsettings import postgressql 
import os
from models import Base, Recipe, Ingredient, Unit, Recipes, Food
from bs4 import BeautifulSoup
import json 

def build_engine(user, passwd, host, port, db):
    try:
        url = f'postgresql://{user}:{passwd}@{host}:{port}/{db}'
        if not database_exists(url):
            create_database(url)
        engine = create_engine(url)
        return(engine)
    except: print("Error: connecting to postgresql")

def check_new_recipes(session):
    try:
        urlpack = check_new_url()
        for line in list(urlpack):
                row = get_html(line)
                name_indb = session.query(Recipe.name).filter(Recipe.name==row['name']).first()
                session.commit()
                if name_indb == None:
                    print(row['name'],' added to database.')
                    entry = Recipe(row['name'], row['url'], row['data'].prettify())
                    session.add(entry)
                    session.commit()
                else: 
                    print(row['name'],' already exists in database.')
                    i += 1
                    if i == 5:
                        break
    except: print('Exception calling check_new_url()')
    i=0
    with open('url_container_pack.txt', 'r') as urlpack:
            for line in urlpack:
                row = get_html(line)
                name_indb = session.query(Recipe.name).filter(Recipe.name==row['name']).first()
                session.commit()
                if name_indb == None:
                    print(row['name'],' added to database.')                  
                    entry = Recipe(row['name'], row['url'], str(row['data']))
                    session.add(entry)
                    session.commit()
                else: 
                    print(row['name'],' already exists in database.')
                    i += 1
                    # Note: algorithm assumes url_container_pack.txt organize in stack datatype (New urls should be stacked on top)
                    if i == 5:
                        break     

def unique_ingredient_list(session):
    for u in session.query(Recipe).all():
        data = {'name':u.name, 'url':u.url, 'data':u.data}
        row_as_dict = dict(data)
        html = row_as_dict['data']
        soup = BeautifulSoup(html, 'html.parser')
        recp_df = get_ingredients(soup)
        ingrd_ls = list(recp_df['ingredient'])
        for item in ingrd_ls:
            mapped_name = ingredient_map(item)
            name_indb = session.query(Ingredient.name).filter(Ingredient.name==mapped_name).first()
            session.commit()            
            if name_indb == None:
                print('adding to database ingrdient: ', mapped_name)
                entry = Ingredient(mapped_name, '')
                session.add(entry)
                session.commit()
            else: print(item, 'already exists in database')

def unique_unit_list(session):
    for u in session.query(Recipe).all():
        data = {'name':u.name, 'url':u.url, 'data':u.data}
        row_as_dict = dict(data)
        html = row_as_dict['data']
        soup = BeautifulSoup(html, 'html.parser')
        recp_df = get_ingredients(soup)
        ingrd_ls = list(recp_df['unit'])
        for item in ingrd_ls:
            if len(item) == 0 : print('no unit listed')
            else:
                name_indb = session.query(Unit.type).filter(Unit.type==item).first()
                session.commit()
                if name_indb == None:
                    print('name_indb is None')
                    try:
                        map_item = unit_word_mapper(item)
                        map_indb = session.query(Unit.type).filter(Unit.type==map_item).first()
                        session.commit()
                        if map_indb == None:
                            print('adding %s to recipe.unit as: %s', item, map_item)
                            entry = Unit(map_item)
                            session.add(entry)
                            session.commit()
                        else: print('mapped name already added.')
                    except: 
                        print('adding %s to recipe.unit', item)
                        entry = Unit(item)
                        session.add(entry)
                        session.commit()
                else: 
                    print(item, 'already exists in database')

def add_foodb(session):
    data = [json.loads(line) for line in open('C:/Users/adeli/Projects/CookingApp/foodb_json/Food.json','r', encoding="utf8")]
    for i in range(len(data)):
        entry = Food(data[i]['name'],data[i]['name_scientific'],data[i]['description'])
        session.add(entry)
        session.commit()
    return print('added dictionary to public.food/recipes/postgres@PostgresSQL15')

def recipe_populate(session):
    from map import amount_dict
    rec_ls = session.query(Recipe._id).all()
    for u in range(len(rec_ls)):
        rec_id = rec_ls[u][0]
        u = session.query(Recipe).filter(Recipe._id==rec_id).first()
        data = {'name':u.name, 'url':u.url, 'data':u.data}
        row_as_dict = dict(data)
        html = row_as_dict['data']
        soup = BeautifulSoup(html, 'html.parser')
        recipe_df = get_ingredients(soup)
        print(recipe_df)
        for i in range((len(recipe_df))):
            recipe_id = session.query(Recipe._id).filter(Recipe.name==u.name).first()
            session.commit()
            if recipe_id:
                recipe_id = recipe_id[0]
            mapped_ingredient = ingredient_map(recipe_df['ingredient'][i])
            if mapped_ingredient == 'breakup':
                mapped_ls = breakup_ingredients(recipe_df['ingredient'][i])
                for g in range(len(mapped_ls)):
                    ingredient_id = session.query(Ingredient._id).filter(Ingredient.name==mapped_ls[g]).first()
                    session.commit()
                    if ingredient_id:
                        ingredient_id = ingredient_id[0]
                    print('recipe_id:', recipe_id, 'amount:none', 'unit_id:none', 'ingredient_id:', ingredient_id)
                    if not(ingredient_id==None):
                        entry = Recipes(recipe_id,None,None,ingredient_id)
                        session.add(entry)
                        session.commit()
            ingredient_id = session.query(Ingredient._id).filter(Ingredient.name==mapped_ingredient).first()
            session.commit()
            if ingredient_id:
                ingredient_id = ingredient_id[0]
            amount = recipe_df['amount'][i]
            if amount in amount_dict:
                amt = amount_dict[amount]
                if type(amt) == list:
                    amount = num_amount(amt[0])
                    unt = amt[1]
                elif not(type(amt) == list):
                    amount = num_amount(amt)
            elif not(amount in amount_dict):
                amount = num_amount(recipe_df['amount'][i])
                unt = recipe_df['unit'][i]
            unit_id = session.query(Unit._id).filter(Unit.type==unit_word_mapper(unt)).first()
            session.commit()
            if unit_id:
                unit_id = unit_id[0]
            print('recipe_id:', recipe_id, 'amount:', amount, 'unit_id:', unit_id, 'ingredient_id:', ingredient_id)
            if not(ingredient_id==None):
                entry = Recipes(recipe_id,amount,unit_id,ingredient_id)
                session.add(entry)
                session.commit()
        

engine = build_engine(postgressql['pguser'], postgressql['pgpass'], postgressql['pghost'], postgressql['pgport'], postgressql['pgdb'])
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
recipe_populate(session)
