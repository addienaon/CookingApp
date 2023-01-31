from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import MyFoodSerializer, IngredientSerializer
from .models import MyFood, Ingredient, Recipes, Recipe
from .forms import MyFoodForm
from django.db.models import Count
# Create your views here.

def myfood_create_view(request):
    obj = MyFood.objects.all()  # Retrieve all existing food items
    if request.method == "POST":
        if "delete" in request.POST:
            # The "delete" button was pressed
            selected_items = request.POST.getlist("selected")  # Get a list of the selected items
            MyFood.objects.filter(pk__in=selected_items).delete()  # Delete the selected items
        else:
            form = MyFoodForm(request.POST)
            if form.is_valid():
                user_input = form.cleaned_data.get('user_input')
                # check if user_input value already exists in obj list
                if not obj.filter(user_input=user_input).exists():
                    form.save()
                else:
                    form.add_error('user_input', 'This food item already exists')
    else:
        form = MyFoodForm()
    context = {
        'form':form,
        'object': obj
    }
    return render(request, "myfood_create.html", context)


def all_ingredients_view(request, *args, **kwargs):
   obj = Ingredient.objects.all()
   context = {
        'object': obj
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


def delete_my_food(request, id):
    food_item = MyFood.objects.get(id=id)
    food_item.delete()
    return redirect("/myfood_create_view")