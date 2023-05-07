from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *
from django.forms.widgets import HiddenInput
from django.contrib.auth.forms import UserCreationForm     
from django.contrib.auth.models import User 

class RecetteForm(forms.ModelForm):
    class Meta:
        model= Recette
        fields= '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control mb-2 '}),
            'temps': forms.NumberInput(attrs={'class': 'form-control mb-2 '}),
            'preparation': forms.TextInput(attrs={'class': 'form-control mb-2 '}),
            'image': forms.FileInput(attrs={'class': 'form-control mb-2 '}),

        }

class IngredientForm(forms.ModelForm):
    class Meta:
        model= Ingredient
        fields = ['recette','name', 'quantity', 'unit']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2  '}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'unit': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        fields = ['user','recette','comment']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control mb-2  '}),
            'recette': forms.Select(attrs={'class': 'form-control mb-2  '}),
            'comment': forms.TextInput(attrs={'class': 'form-control mb-2  '}),
        }
    


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','first_name','password1','password2']

   