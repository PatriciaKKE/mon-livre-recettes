from rest_framework import generics
from .models import Recette
from .serializers import RecipeSerializer

class RecipeListCreate(generics.ListCreateAPIView):
    queryset = Recette.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recette.objects.all()
    serializer_class = RecipeSerializer
