
from django.shortcuts import redirect, render
from .models import MyFood, Recipes, Recipe, Ingredient, Nutrition
from django.db.models import Count, F
from django.views.generic import ListView
# from django.urls import reverse

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredient_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # group the ingredients by category
        categories = {}
        for ingredient in context['object_list']:
            if ingredient.category:
                if ingredient.category.name not in categories:
                    categories[ingredient.category.name] = []
                categories[ingredient.category.name].append(ingredient)
        # sort the category names alphabetically
        sorted_categories = {k: sorted(v, key=lambda i: i.name) for k, v in sorted(categories.items())}
        context['categories'] = sorted_categories
        return context
    
    def post(self, request, *args, **kwargs):
        # Get all selected ingredients
        selected_ingredients = request.POST.getlist('ingredients')
        # Create a MyFood object for each selected ingredient
        for ingredient_id in selected_ingredients:
            ingredient = Ingredient.objects.get(pk=ingredient_id)
            if MyFood.objects.filter(fk_ingredient=ingredient).exists():
                print(f"{ingredient.name} already exists in MyFood")
            else:
                my_food = MyFood.objects.create(
                    user_input=ingredient.name,
                    fk_ingredient=ingredient,
                    selected=True,
                )
                my_food.save()
        return redirect('myfood')


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

    matched_recipes = sorted(matched_recipes, key=lambda r: r.name)

    context = {'object':matched_recipes}

    return render(request, "recipes.html", context)


def myfood_view(request):
    myfood = MyFood.objects.all().select_related('fk_ingredient').order_by('fk_ingredient__category__name', 'fk_ingredient__name')
    categories = {}
    for item in myfood:
        category = item.fk_ingredient.category
        if category:
            if category.name not in categories:
                categories[category.name] = []
            categories[category.name].append(item)

    if request.method == 'POST':
        selected_items = request.POST.getlist('selected')
        MyFood.objects.filter(pk__in=selected_items).delete()
        return redirect('myfood')

    context = {
        'categories': categories,
    }
    return render(request, 'myfood.html', context)



def delete_my_food(request):
    if request.method == 'POST':
        selected_items = request.POST.getlist('selected')
        for item_id in selected_items:
            food_item = MyFood.objects.get(id=item_id)
            food_item.delete()
    return redirect('myfood')

def single_recipe_view(request, id, name):
    recipe = Recipe.objects.filter(id=id) \
        .annotate(ingredient_name=F('recipes__ingredient__name'), amount=F('recipes__amount'), unit_type=F('recipes__unit__type'), recipe_cuisine=F('cuisine'), recipe_servings=F('servings')) \
        .values('name', 'url', 'id', 'recipe_cuisine', 'recipe_servings', 'ingredient_name', 'amount', 'unit_type')

    nutrition_data = Nutrition.objects.filter(recipe__id=id) \
        .annotate(
            calories_unit_type=F('calories_unit__type'),
            carbohydrates_unit_type=F('carbohydrates_unit__type'),
            protein_unit_type=F('protein_unit__type'),
            fat_unit_type=F('fat_unit__type'),
            saturated_fat_unit_type=F('saturated_fat_unit__type'),
            polyunsaturated_fat_unit_type=F('polyunsaturated_fat_unit__type'),
            monounsaturated_fat_unit_type=F('monounsaturated_fat_unit__type'),
            trans_fat_unit_type=F('trans_fat_unit__type'),
            cholesterol_unit_type=F('cholesterol_unit__type'),
            sodium_unit_type=F('sodium_unit__type'),
            potassium_unit_type=F('potassium_unit__type'),
            fiber_unit_type=F('fiber_unit__type'),
            sugar_unit_type=F('sugar_unit__type'),
            vitamin_a_unit_type=F('vitamin_a_unit__type'),
            vitamin_c_unit_type=F('vitamin_c_unit__type'),
            calcium_unit_type=F('calcium_unit__type'),
            iron_unit_type=F('iron_unit__type'),
        ) \
        .values(
            'calories_amount', 'calories_unit_type',
            'carbohydrates_amount', 'carbohydrates_unit_type',
            'protein_amount', 'protein_unit_type',
            'fat_amount', 'fat_unit_type',
            'saturated_fat_amount', 'saturated_fat_unit_type',
            'polyunsaturated_fat_amount', 'polyunsaturated_fat_unit_type',
            'monounsaturated_fat_amount', 'monounsaturated_fat_unit_type',
            'trans_fat_amount', 'trans_fat_unit_type',
            'cholesterol_amount', 'cholesterol_unit_type',
            'sodium_amount', 'sodium_unit_type',
            'potassium_amount', 'potassium_unit_type',
            'fiber_amount', 'fiber_unit_type',
            'sugar_amount', 'sugar_unit_type',
            'vitamin_a_amount', 'vitamin_a_unit_type',
            'vitamin_c_amount', 'vitamin_c_unit_type',
            'calcium_amount', 'calcium_unit_type',
            'iron_amount', 'iron_unit_type'
        )

    recipe_data = [
        {
            'recipe_name': ingredient['name'],
            'recipe_url': ingredient['url'],
            'recipe_cuisine': ingredient['recipe_cuisine'],
            'recipe_servings': ingredient['recipe_servings'],
            'ingredient_name': ingredient['ingredient_name'],
            'amount': ingredient['amount'] if ingredient['amount'] is not None else '',
            'unit_type': ingredient['unit_type'] if ingredient['unit_type'] is not None else '',
        }
        for ingredient in recipe
    ]

    context = {
        'recipe': recipe_data,
        'nutrition': nutrition_data
    }

    return render(request, "recipe.html", context)





