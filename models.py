from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Float
from sqlalchemy.dialects.mysql import VARCHAR

Base = declarative_base()

class Recipe(Base):
    __tablename__ = "recipe"
    _id = Column("id", Integer, primary_key=True)
    name = Column(String(255).with_variant(VARCHAR(255, charset="utf8"), "mysql"))
    url = Column(String(500).with_variant(VARCHAR(255, charset="utf8"), "mysql"))
    data = Column(String)
    cuisine = Column(String(255))
    servings = Column(Float)

    def __init__(self, name, url, data, cuisine, servings):
        self.name = name
        self.url = url
        self.data = data
        self.cuisine = cuisine
        self.servings = servings

    def __repr__(self):
        return f"({self.name} {self.url} {self.data} {self.cuisine} {self.servings})"


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

    def __init__(self, type):
        self.type = type

class Recipes(Base):
    __tablename__= "recipes"
    _id = Column("id", Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    amount = Column(Float)
    unit_id = Column(Integer, ForeignKey('unit.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredient.id')) 

    def __init__(self, recipe_id, amount, unit_id, ingredient_id):
        self.recipe_id = recipe_id
        self.amount = amount
        self.unit_id = unit_id
        self.ingredient_id = ingredient_id

class Food(Base):
    __tablename__= "food"
    _id = Column("id", Integer, primary_key=True)
    name = Column(String(255).with_variant(VARCHAR(255, charset="utf8"), "mysql"))
    name_scientific = Column(String(255).with_variant(VARCHAR(255, charset="utf8"), "mysql"))
    description = Column(String)

    def __init__(self, name, name_scientific, description):
        self.name = name
        self.name_scientific = name_scientific
        self.description = description

class Nutrition(Base):
    __tablename__ = "nutrition"
    _id = Column("id", Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipe.id"))
    calories_amount = Column(Float)
    calories_unit_id = Column(Integer, ForeignKey("unit.id"))
    carbohydrates_amount = Column(Float)
    carbohydrates_unit_id = Column(Integer, ForeignKey("unit.id"))
    protein_amount = Column(Float)
    protein_unit_id = Column(Integer, ForeignKey("unit.id"))
    fat_amount = Column(Float)
    fat_unit_id = Column(Integer, ForeignKey("unit.id"))
    saturated_fat_amount = Column(Float)
    saturated_fat_unit_id = Column(Integer, ForeignKey("unit.id"))
    polyunsaturated_fat_amount = Column(Float)
    polyunsaturated_fat_unit_id = Column(Integer, ForeignKey("unit.id"))
    monounsaturated_fat_amount = Column(Float)
    monounsaturated_fat_unit_id = Column(Integer, ForeignKey("unit.id"))
    trans_fat_amount = Column(Float)
    trans_fat_unit_id = Column(Integer, ForeignKey("unit.id"))
    cholesterol_amount = Column(Float)
    cholesterol_unit_id = Column(Integer, ForeignKey("unit.id"))
    sodium_amount = Column(Float)
    sodium_unit_id = Column(Integer, ForeignKey("unit.id"))
    potassium_amount = Column(Float)
    potassium_unit_id = Column(Integer, ForeignKey("unit.id"))
    fiber_amount = Column(Float)
    fiber_unit_id = Column(Integer, ForeignKey("unit.id"))
    sugar_amount = Column(Float)
    sugar_unit_id = Column(Integer, ForeignKey("unit.id"))
    vitamin_a_amount = Column(Float)
    vitamin_a_unit_id = Column(Integer, ForeignKey("unit.id"))
    vitamin_c_amount = Column(Float)
    vitamin_c_unit_id = Column(Integer, ForeignKey("unit.id"))
    calcium_amount = Column(Float)
    calcium_unit_id = Column(Integer, ForeignKey("unit.id"))
    iron_amount = Column(Float)
    iron_unit_id = Column(Integer, ForeignKey("unit.id"))

    def __init__(
        self,
        recipe_id,
        calories_amount,
        calories_unit_id,
        carbohydrates_amount,
        carbohydrates_unit_id,
        protein_amount,
        protein_unit_id,
        fat_amount,
        fat_unit_id,
        saturated_fat_amount,
        saturated_fat_unit_id,
        polyunsaturated_fat_amount,
        polyunsaturated_fat_unit_id,
        monounsaturated_fat_amount,
        monounsaturated_fat_unit_id,
        trans_fat_amount,
        trans_fat_unit_id,
        cholesterol_amount,
        cholesterol_unit_id,
        sodium_amount,
        sodium_unit_id,
        potassium_amount,
        potassium_unit_id,
        fiber_amount,
        fiber_unit_id,
        sugar_amount,
        sugar_unit_id,
        vitamin_a_amount,
        vitamin_a_unit_id,
        vitamin_c_amount,
        vitamin_c_unit_id,
        calcium_amount,
        calcium_unit_id,
        iron_amount,
        iron_unit_id,
    ):
        self.recipe_id = recipe_id
        self.calories_amount = calories_amount
        self.calories_unit_id = calories_unit_id
        self.carbohydrates_amount = carbohydrates_amount
        self.carbohydrates_unit_id = carbohydrates_unit_id
        self.protein_amount = protein_amount
        self.protein_unit_id = protein_unit_id
        self.fat_amount = fat_amount
        self.fat_unit_id = fat_unit_id
        self.saturated_fat_amount = saturated_fat_amount
        self.saturated_fat_unit_id = saturated_fat_unit_id
        self.polyunsaturated_fat_amount = polyunsaturated_fat_amount
        self.polyunsaturated_fat_unit_id = polyunsaturated_fat_unit_id
        self.monounsaturated_fat_amount = monounsaturated_fat_amount
        self.monounsaturated_fat_unit_id = monounsaturated_fat_unit_id
        self.trans_fat_amount = trans_fat_amount
        self.trans_fat_unit_id = trans_fat_unit_id
        self.cholesterol_amount = cholesterol_amount
        self.cholesterol_unit_id = cholesterol_unit_id
        self.sodium_amount = sodium_amount
        self.sodium_unit_id = sodium_unit_id
        self.potassium_amount = potassium_amount
        self.potassium_unit_id = potassium_unit_id
        self.fiber_amount = fiber_amount
        self.fiber_unit_id = fiber_unit_id
        self.sugar_amount = sugar_amount
        self.sugar_unit_id = sugar_unit_id
        self.vitamin_a_amount = vitamin_a_amount
        self.vitamin_a_unit_id = vitamin_a_unit_id
        self.vitamin_c_amount = vitamin_c_amount
        self.vitamin_c_unit_id = vitamin_c_unit_id
        self.calcium_amount = calcium_amount
        self.calcium_unit_id = calcium_unit_id
        self.iron_amount = iron_amount
        self.iron_unit_id = iron_unit_id

    def __str__(self):
        return f"{self.recipe_id}\n\
    {self.calories_amount} {self.calories_unit_id}\n\
    {self.carbohydrates_amount} {self.carbohydrates_unit_id}\n\
    {self.protein_amount} {self.protein_unit_id}\n\
    {self.fat_amount} {self.fat_unit_id}\n\
    {self.saturated_fat_amount} {self.saturated_fat_unit_id}\n\
    {self.polyunsaturated_fat_amount} {self.polyunsaturated_fat_unit_id}\n\
    {self.monounsaturated_fat_amount} {self.monounsaturated_fat_unit_id}\n\
    {self.trans_fat_amount} {self.trans_fat_unit_id}\n\
    {self.cholesterol_amount} {self.cholesterol_unit_id}\n\
    {self.sodium_amount} {self.sodium_unit_id}\n\
    {self.potassium_amount} {self.potassium_unit_id}\n\
    {self.fiber_amount} {self.fiber_unit_id}\n\
    {self.sugar_amount} {self.sugar_unit_id}\n\
    {self.vitamin_a_amount} {self.vitamin_a_unit_id}\n\
    {self.vitamin_c_amount} {self.vitamin_c_unit_id}\n\
    {self.calcium_amount} {self.calcium_unit_id}\n\
    {self.iron_amount} {self.iron_unit_id}"

