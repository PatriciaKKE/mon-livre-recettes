from rest_framework import serializers
from .models import Recette

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recette
        fields = '__all__'
