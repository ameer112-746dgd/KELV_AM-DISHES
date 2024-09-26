from django.shortcuts import render
from my_app.models import Recipe


def home_request(request):
    recipes = Recipe.objects.all()  # Fetch all recipes
    return render(request, 'recipe_home.html', {'recipes': recipes})
