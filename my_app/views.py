from django.shortcuts import render, redirect
from my_app.models import Recipe
from .forms import RecipeForm

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'media_list.html', {'recipes': recipes})

def upload_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'upload.html', {'form': form})
