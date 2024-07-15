from django.db import models

# Create your models here.


class IngredientCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(IngredientCategory, related_name='category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



