from django.contrib import admin
from django.urls import path, include
from whats_in_fridge.views import IngredientListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingredients/', IngredientListView.as_view(), name='ingredients'),
    path('', include('whats_in_fridge.urls')),
]