from rest_framework import serializers
from .models import MyFood, Ingredient, Recipes

class MyFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyFood
        fields = ['id', 'user_input', 'fk_ingredient', 'selected']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'type']

class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ['id', 'recipe', 'amount', 'unit', 'ingredient']