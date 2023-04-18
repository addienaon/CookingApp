# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=255)
    name_scientific = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food'


class Fridge(models.Model):
    ingredients = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fridge'

class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'

        
class Ingredient(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ingredient'


class Recipe(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(unique=True, max_length=500, blank=True, null=True)
    data = models.TextField(blank=True, null=True)

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

