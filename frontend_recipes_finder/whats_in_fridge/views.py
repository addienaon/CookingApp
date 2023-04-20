from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import MyFoodSerializer, IngredientSerializer
from .models import MyFood, Ingredient, Recipes, Recipe, Category
from .forms import MyFoodForm
from django.db.models import Count, F, Q
# Create your views here.

def create_myfood_view(request):
    myfood_data = MyFood.objects.all()  # Retrieve all existing food items
    myfood_categories = set(i.fk_ingredient.category.name for i in myfood_data.all())
    myfood_categories = sorted(list(myfood_categories))
    if request.method == "POST":
        form = MyFoodForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data.get('user_input')
                # check if user_input value already exists in obj list
            if not myfood_data.filter(user_input=user_input).exists():
                form.save()
            else:
                form.add_error('user_input', 'This food item already exists')
    else:
        form = MyFoodForm()
    myfood_data = [
        {
            'id': food.id,
            'user_input': food.user_input,
            'selected': food.selected,
            'type': food.fk_ingredient.category.name,
        }
        for food in myfood_data
    ]
    context = {
        'form':form,
        'myfood_data': myfood_data, 
        'myfood_categories': myfood_categories

    }
    return render(request, "myfood_create.html", context)


def all_ingredients_view(request, *args, **kwargs):
    obj = Ingredient.objects.all()
   
    ingredient_data = [
        {
            'id': ingredient.id,
            'name': ingredient.name,
            'type': ingredient.category.name,
        
        }
        
        for ingredient in obj
    ]
    ingredient_categories = set(ingredient.category.name for ingredient in obj)
    ingredient_categories = sorted(list(ingredient_categories))

    context = {
        'ingredient_data': ingredient_data,
        'ingredient_categories': ingredient_categories,
    }
    return render(request, "ingredients.html", context)
  


def recipes_view(request, *args, **kwargs):
    ingredient_count = Recipes.objects.values('recipe_id').annotate(count=Count('ingredient')).order_by('recipe_id')

    recipes = Recipe.objects.filter(recipes__ingredient__in=MyFood.objects.values('fk_ingredient'))\
            .annotate(myfood_ingredient_count=Count('name'))\
            .filter(myfood_ingredient_count__in=ingredient_count.values_list('count', flat=True))\
            .values('name', 'id', 'myfood_ingredient_count')

    matched_recipes = []

    for recipe in recipes:
        recipe_id = recipe['id']
        myfood_ing_count = recipe['myfood_ingredient_count']
        ing_count_obj = [x for x in ingredient_count if x['recipe_id'] == recipe_id]
        ing_count = ing_count_obj[0]['count'] if ing_count_obj else 0
        if myfood_ing_count == ing_count:
            matched_recipes.append(Recipe.objects.get(id=recipe_id))    

    context = {'object':matched_recipes}

    return render(request, "recipes.html", context)


def delete_my_food(request):
    if request.method == 'POST':
        id_list = request.POST.getlist("selected")
        for food_item in id_list:
            food_item = int(food_item)
            MyFood.objects.filter(pk=food_item).delete()
    return redirect("/myfood/create")

def add_ingredients(request):
    if request.method == 'POST':
        id_list = request.POST.getlist("selected")
        for ingredient_id in id_list:
            ingredient_id = int(ingredient_id)
            ingredient = Ingredient.objects.filter(pk=ingredient_id).first()
            MyFood.objects.create(fk_ingredient=ingredient, user_input=ingredient.name)
    return redirect("/ingredients")

def single_recipe_view(request, id, name):
    recipe = Recipe.objects.filter(id=id) \
    .annotate(ingredient_name=F('recipes__ingredient__name'), amount=F('recipes__amount'), unit_type=F('recipes__unit__type')) \
    .values('name', 'id', 'ingredient_name', 'amount', 'unit_type')
    print(recipe)
    recipe_data = [
    {
        'recipe_name': ingredient['name'],
        'ingredient_name': ingredient['ingredient_name'],
        'amount': ingredient['amount'] if ingredient['amount'] is not None else '',
        'unit_type': ingredient['unit_type'] if ingredient['unit_type'] is not None else '',
    }
    for ingredient in recipe
    ]

    context = { 
        'recipe':recipe_data,
    }
    
    return render(request, "recipe.html", context)

