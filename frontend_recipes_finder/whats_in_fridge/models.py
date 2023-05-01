from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category'


class Food(models.Model):
    name = models.CharField(max_length=255)
    name_scientific = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food'


class Ingredient(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    selected = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredient'


class MyFood(models.Model):
    user_input = models.CharField(max_length=255)
    fk_ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING, blank=True, null=True)
    selected = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_food'


class Nutrition(models.Model):
    recipe = models.ForeignKey('Recipe', models.DO_NOTHING, blank=True, null=True)
    calories_amount = models.FloatField(blank=True, null=True)
    calories_unit = models.ForeignKey('Unit', models.DO_NOTHING, blank=True, null=True)
    carbohydrates_amount = models.FloatField(blank=True, null=True)
    carbohydrates_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_carbohydrates_unit_set', blank=True, null=True)
    protein_amount = models.FloatField(blank=True, null=True)
    protein_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_protein_unit_set', blank=True, null=True)
    fat_amount = models.FloatField(blank=True, null=True)
    fat_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_fat_unit_set', blank=True, null=True)
    saturated_fat_amount = models.FloatField(blank=True, null=True)
    saturated_fat_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_saturated_fat_unit_set', blank=True, null=True)
    polyunsaturated_fat_amount = models.FloatField(blank=True, null=True)
    polyunsaturated_fat_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_polyunsaturated_fat_unit_set', blank=True, null=True)
    monounsaturated_fat_amount = models.FloatField(blank=True, null=True)
    monounsaturated_fat_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_monounsaturated_fat_unit_set', blank=True, null=True)
    trans_fat_amount = models.FloatField(blank=True, null=True)
    trans_fat_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_trans_fat_unit_set', blank=True, null=True)
    cholesterol_amount = models.FloatField(blank=True, null=True)
    cholesterol_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_cholesterol_unit_set', blank=True, null=True)
    sodium_amount = models.FloatField(blank=True, null=True)
    sodium_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_sodium_unit_set', blank=True, null=True)
    potassium_amount = models.FloatField(blank=True, null=True)
    potassium_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_potassium_unit_set', blank=True, null=True)
    fiber_amount = models.FloatField(blank=True, null=True)
    fiber_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_fiber_unit_set', blank=True, null=True)
    sugar_amount = models.FloatField(blank=True, null=True)
    sugar_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_sugar_unit_set', blank=True, null=True)
    vitamin_a_amount = models.FloatField(blank=True, null=True)
    vitamin_a_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_vitamin_a_unit_set', blank=True, null=True)
    vitamin_c_amount = models.FloatField(blank=True, null=True)
    vitamin_c_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_vitamin_c_unit_set', blank=True, null=True)
    calcium_amount = models.FloatField(blank=True, null=True)
    calcium_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_calcium_unit_set', blank=True, null=True)
    iron_amount = models.FloatField(blank=True, null=True)
    iron_unit = models.ForeignKey('Unit', models.DO_NOTHING, related_name='nutrition_iron_unit_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nutrition'


class Recipe(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(unique=True, max_length=500, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    cuisine = models.CharField(max_length=255, blank=True, null=True)
    servings = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe'


class Recipes(models.Model):
    recipe = models.ForeignKey(Recipe, models.DO_NOTHING)
    amount = models.FloatField(blank=True, null=True)
    unit = models.ForeignKey('Unit', models.DO_NOTHING, blank=True, null=True)
    ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recipes'


class Unit(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unit'