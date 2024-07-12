from django.db import models

# Create your models here.


class IngredientCategory(models.Model):
    name = models.CharField(max_length=50)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(IngredientCategory, related_name='category')



