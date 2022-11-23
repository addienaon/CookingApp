from sqlalchemy import create_engine, insert, Column, String, Integer
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
import pyodbc
import pandas as pd
from scrapfun import get_html, get_container_pack, check_new_url
from localsettings import postgressql 
import os

#get user and password from environment var

#SQLAlchemy
#When using recipe class on another script ##from etl import Base, recipe
Base = declarative_base()

class recipe(Base):
    __tablename__ = "recipe"
    _id = Column("id", Integer, primary_key=True)
    name = Column(String(255).with_variant(VARCHAR(255, charset="utf8"), "mysql"))
    url = Column(String(500).with_variant(VARCHAR(255, charset="utf8"), "mysql"))
    data = Column(String)

    def __init__(self, name, url, data):
        self.name = name
        self.url = url
        self.data = data

    def __repr__(self):
        return f"({self.name} {self.url} {self.data})"

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
                name_indb = session.query(recipe.name).filter(recipe.name==row['name']).first()
                session.commit()
                if name_indb == None:
                    print(row['name'],' added to database.')
                    entry = recipe(row['name'], row['url'], row['data'].prettify())
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
                name_indb = session.query(recipe.name).filter(recipe.name==row['name']).first()
                session.commit()
                if name_indb == None:
                    print(row['name'],' added to database.')
                    entry = recipe(row['name'], row['url'], row['data'].prettify())
                    session.add(entry)
                    session.commit()
                else: 
                    print(row['name'],' already exists in database.')
                    i += 1
                    # Note: algorithm assumes url_container_pack.txt organize in stack datatype (New urls should be stacked on top)
                    if i == 5:
                        break
engine = build_engine(postgressql['pguser'], postgressql['pgpass'], postgressql['pghost'], postgressql['pgport'], postgressql['pgdb'])
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()            
check_new_recipes(session)