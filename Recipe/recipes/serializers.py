from rest_framework import serializers

from recipes.models import Recipes


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipes
        fields="__all__"