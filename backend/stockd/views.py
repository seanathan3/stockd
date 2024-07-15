from django.shortcuts import render
from .models import Ingredient

# Create your views here.

def index(request):
    ingredients = Ingredient.objects.all()
    return render(request, "stockd/index.html", {"ingredients": ingredients})

