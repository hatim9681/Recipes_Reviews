from django.urls import path, include
from django.urls import re_path as url
from .views import *
from django.contrib import admin
urlpatterns = [
    path('recettes/', recettes_list, name='recettes'),
    path('list_clients/', list_clients, name='list_clients'),
    path('ingredients/', ingredients_list, name='ingredients'),
    path('create_recette/', create_recette, name='create_recette'),
    path('create_ingredient/<int:id>', create_ingredient, name='create_ingredient'),
    path('search_recette/', search_recette, name='search_recette'),
    path('search_ingredient/', search_ingredient, name='search_ingredient'),
    path('delete_recette/<int:id>', delete_recette, name='delete_recette'),
    path('delete_ingredient/<int:id>',
         delete_ingredient, name='delete_ingredient'),
    path('update_recette/<int:id>', update_recette, name='update_recette'),
    path('update_ingredient/<int:id>',
         update_ingredient, name='update_ingredient'),
    path('recette_info/<int:id>', recette_info, name='recette_info'),
    path('register/',register,name='register' ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',home,name='home' ),

]
