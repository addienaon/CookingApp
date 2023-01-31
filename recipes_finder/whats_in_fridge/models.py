from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=255)
    name_scientific = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food'

class Ingredient(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)

    # def __str__(self):
    #     return self.name

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

    def __str__(self):
        return self.recipe.name

class Unit(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unit'


class MyFood(models.Model):
    user_input = models.CharField(max_length=255, blank=True, null=True)
    fk_ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    selected = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'my_food'
