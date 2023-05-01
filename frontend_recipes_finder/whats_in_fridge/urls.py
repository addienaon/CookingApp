from django.urls import path
from .views import delete_my_food, myfood_view, recipes_view, single_recipe_view

urlpatterns = [
    #path('create/', create_myfood_view, name='createfood'),
    #path('add_ingredients/', add_ingredients, name='add_ingredients'),
    # path('recipes/<int:id>/<slug:name>/', recipes_view, name='recipes')
    path('deletefood/', delete_my_food, name='delete_my_food'),
    path('myfood/', myfood_view, name='myfood'),
    path('recipes/', recipes_view, name='recipes'),
    path('recipe/<int:id>/<str:name>/', single_recipe_view, name='single_recipe')

   
]