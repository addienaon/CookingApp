from sqlalchemy import create_engine, insert
import pyodbc
import pandas as pd
import os

#get user and password from environment var
# psw = os.environ['PGPASS'] #'g3Twenty!'
# uid = os.environ['PGPUSER'] #'etl'

# #extract data with web scrapper

# #load data to postgres
# db = create_engine(f'postgresql://{uid}:{psw}@localhost:5432/recipees')
# db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")  
# db.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

print(os.environ.get('PGPASS'))