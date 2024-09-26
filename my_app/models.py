# from django.db import models

# class Recipe(models.Model):
#     title = models.CharField(max_length=200)
#     prep_time = models.DurationField()  # Use DurationField for preparation time
#     description = models.TextField(blank=True)
#     ingredients = models.TextField()  # Store ingredients as a text field
#     instructions = models.TextField()  # Store instructions as a text field
#     image = models.ImageField(upload_to='recipes/')  # Use ImageField for recipe images
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
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='breakfast')

    def __str__(self):
        return self.title
