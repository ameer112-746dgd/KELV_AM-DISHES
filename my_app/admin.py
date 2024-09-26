# # Register your models here.

# from django.contrib import admin
# from .models import Recipe

# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('title', 'prep_time', 'description', 'image')

# admin.site.register(Recipe, RecipeAdmin)


from django.contrib import admin
from .models import Recipe  # Import the Recipe model from models.py

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'prep_time', 'category', 'image')
    search_fields = ('title',)
    list_filter = ('category',)
    fields = ('title', 'prep_time', 'description', 'ingredients', 'instructions', 'image', 'upload_video', 'category')

admin.site.register(Recipe, RecipeAdmin)  # Register the Recipe model
