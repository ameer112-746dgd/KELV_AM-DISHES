# from django.shortcuts import render
# from .models import Recipe

# # Create your views here.
# def home_views(request):
#     recipes = Recipe.objects.all()
#     context = {
#         'recipes': recipes
#     }
    
#     return render(request, 'index.html', context)


from django.shortcuts import render
from .models import Recipe

def home_views(request):
    featured_recipes = Recipe.objects.all()  # Fetch all recipes for featured
    breakfast_recipes = Recipe.objects.filter(category='breakfast')  # Filter for breakfast
    lunch_recipes = Recipe.objects.filter(category='lunch')  # Filter for lunch
    dinner_recipes = Recipe.objects.filter(category='dinner')  # Filter for dinner
    
    context = {
        'recipes': featured_recipes,
        'breakfast_recipes': breakfast_recipes,
        'lunch_recipes': lunch_recipes,
        'dinner_recipes': dinner_recipes,
    }
    
    return render(request, 'index.html', context)
