"""recipes_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from whats_in_fridge.views import all_ingredients_view, myfood_create_view, recipes_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingredients/', all_ingredients_view, name='all ingredients'),
    path('myfood/', myfood_create_view),
    path('recipes/', recipes_view),
    # path('fridge/', include('whats_in_fridge.urls'))
]