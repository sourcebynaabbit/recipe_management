from django.shortcuts import render
from .models import Recipe
from rest_framework import generics
from .serializers import RecipeSerializer
# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html',{'recipes':recipes})

class AllRecipes(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


