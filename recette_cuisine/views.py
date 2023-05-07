from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .form import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

# liste



def recettes_list(request):
    recettes = Recette.objects.all()
    return render(request, 'recettes.html', {'recettes': recettes})


def list_clients(request):
    recettes = Recette.objects.all()
    return render(request, 'recettes_clients.html', {'recettes': recettes})


def ingredients_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredients.html', {'ingredients': ingredients})


def recette_info(request, id):
    recette = get_object_or_404(Recette, id=id)
    intaial_data={
        'recette':recette
    }
    ingredients = Ingredient.objects.filter(recette_id=id)
    reviews = Review.objects.filter(recette=id)
    count=reviews.count()

    if request.method == 'POST': 
        form=ReviewForm(request.POST)
        if form.is_valid():
            form.save()    
            return redirect('recette_info',id)
    else:
        form=ReviewForm()

    return render(request, 'une_recette.html', {'recette': recette, 'count': count,'reviews': reviews, 'ingredients': ingredients,'form': form})

# create

# recette


def create_recette(request):
    if request.method == 'POST':
        form = RecetteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_clients')
    else:
        form = RecetteForm()

    return render(request, 'create_recette.html', {'form': form})
# ingredient


def create_ingredient(request,id):
    recette = get_object_or_404(Recette, id=id)
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'create_ingredient.html', {'form': form ,'recette': recette})
    else:
        form = IngredientForm()
    return render(request, 'create_ingredient.html', {'form': form ,'recette': recette})

# review





# update


def update_recette(request, id):
    recette = get_object_or_404(Recette, id=id)
    if request.method == 'POST':
        form = RecetteForm(request.POST, request.FILES, instance=recette)
        if form.is_valid():
            form.save()
            return redirect('list_clients')
    else:
        form = RecetteForm(instance=recette)
    return render(request, 'update_recette.html', {'form': form, 'recette': recette})


def update_ingredient(request, id):
    ingredient = get_object_or_404(Ingredient, id=id)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredients')
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'update_ingredient.html', {'form': form, 'ingredient': ingredient})
# delete

@login_required
def delete_recette(request, id):
    recette = get_object_or_404(Recette, id=id)
    recette.delete()
    return redirect('list_clients')


def delete_ingredient(request, id):
    ingredient = get_object_or_404(Ingredient, id=id)
    id1=ingredient.recette.id
    ingredient.delete()
    return redirect('recette_info',id1)
# search


def search_recette(request):
    keyW = request.GET.get('kw')
    recettes = Recette.objects.filter(nom__contains=keyW)
    return render(request, 'recettes_clients.html', {'recettes': recettes})


def search_ingredient(request):
    keyW = request.GET.get('kw')
    ingredients = Ingredient.objects.filter(name__contains=keyW)
    return render(request, 'ingredients.html', {'ingredients': ingredients})


#authen

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})