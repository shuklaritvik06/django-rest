from rest_framework import serializers
from .models import Chef, Recipes


class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = "__all__"


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = "__all__"
