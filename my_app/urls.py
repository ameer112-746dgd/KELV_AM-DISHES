from django.urls import path
from .views import recipe_list, upload_recipe
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('recipes/', recipe_list, name='recipe_list'),
    path('upload/', upload_recipe, name='upload_recipe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
