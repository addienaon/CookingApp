
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingredients/', all_ingredients_view, name='all ingredients'),
    path('recipes/', recipes_view, name='recipes'),
    path('recipe/<int:id>/<str:name>/', single_recipe_view, name='single_recipe'),
    path('myfood/', include('whats_in_fridge.urls'))
]