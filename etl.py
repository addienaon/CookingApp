from sqlalchemy import create_engine, insert
import pyodbc
import pandas as pd
import os

#get user and password from environment var
psw = os.environ['PGPASS']
uid = os.environ['PGPUSER']

#extract data with web scrapper

#load data to postgres
def load():
    try:
        engine = create_engine(f'postgresql://{uid}:{psw}@localhost:5432/recipees')