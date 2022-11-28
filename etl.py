from sqlalchemy import create_engine, insert, select, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import pyodbc
import pandas as pd
from scrapfun import get_html, get_container_pack, check_new_url, get_ingredients
from localsettings import postgressql 
import os
from models import Base, Recipe, Ingredient, Unit


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
                    entry = Recipe(row['name'], row['url'], row['data'].prettify())
                    session.add(entry)
                    session.commit()
                else: 
                    print(row['name'],' already exists in database.')
                    i += 1
                    # Note: algorithm assumes url_container_pack.txt organize in stack datatype (New urls should be stacked on top)
                    if i == 5:
                        break     

def add_ingredients(session):
    ####CYCLE THROUGH RECIPE NAMES AND GET EACH RECIPES INGREDIENT CHECK IF NOT EXISTS IN INGREDIENTS.NAME AND ADD IF NOT
    recipe_list = session.query(Recipe).all()
    session.commit()
    ingredient_list = session.query(Ingredient).all()
    ingredient_set = set()
    for row in recipe_list: 
        new_ingredeints = set(get_ingredients(row.data))
        for ingredient in ingredient_list: ingredient_set.append(ingredient.name)
        inter = new_ingredeints.difference(ingredient_set)

engine = build_engine(postgressql['pguser'], postgressql['pgpass'], postgressql['pghost'], postgressql['pgport'], postgressql['pgdb'])
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()