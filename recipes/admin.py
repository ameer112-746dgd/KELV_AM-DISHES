from django.contrib import admin
from .models import Recipe  # Import the Recipe model from models.py

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'prep_time', 'category', 'image')  # Include category in the display
    search_fields = ('title',)  # Allow searching by title
    list_filter = ('category',)  # Add category filter in the admin panel
    fields = ('title', 'prep_time', 'description', 'ingredients', 'instructions', 'image', 'upload_video', 'category')  # Include category in form

admin.site.register(Recipe, RecipeAdmin)  # Register the Recipe model with the admin site
