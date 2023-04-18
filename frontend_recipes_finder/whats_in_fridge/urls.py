from django.urls import path
from .views import create_myfood_view, delete_my_food, add_ingredients

urlpatterns = [
    path('create/', create_myfood_view, name='createfood'),
    path('deletefood/', delete_my_food, name='deletefood'),
    path('add_ingredients/', add_ingredients, name='add_ingredients'),
]