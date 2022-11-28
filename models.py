from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, insert, Column, String, Integer, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR

Base = declarative_base()

class Recipe(Base):
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

class Ingredient(Base):
    __tablename__= "ingredient"
    _id = Column("id", Integer, primary_key=True)
    name = Column(String(255).with_variant(VARCHAR(255, charset="utf8"), "mysql"))
    type = Column(String(50).with_variant(VARCHAR(50, charset="utf8"), "mysql"))

    def __init__(self, name, type):
        self.name = name
        self.type = type
    
class Unit(Base):
    __tablename__="unit"
    _id = Column("id", Integer, primary_key=True)
    type = Column(String(50).with_variant(VARCHAR(50, charset="utf8"), "mysql"))

class Recipes(Base):
    __tablename__= "recipes"
    recipe_id = Column(Integer, primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingrdient.id'))
    amount = Column(Integer)
    unit_id = Column(Integer, ForeignKey('unit.id')) 
