# from django.db import models

# class Recipe(models.Model):
#     title = models.CharField(max_length=200)
#     prep_time = models.DurationField()
#     description = models.TextField(blank=True)
#     ingredients = models.TextField()
#     instructions = models.TextField()
#     image = models.ImageField(upload_to='recipes/')
#     upload_video = models.FileField(upload_to='videos/', null=True, blank=True)

#     def __str__(self):
#         return self.title


from django.db import models

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]
    
    title = models.CharField(max_length=200)
    prep_time = models.DurationField()
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/')
    upload_video = models.FileField(upload_to='videos/', null=True, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='breakfast')  # Add category field

    def __str__(self):
        return self.title
