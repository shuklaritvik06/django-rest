from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Chef, Recipes
from django.forms.models import model_to_dict
from .serializers import ChefSerializer, RecipeSerializer

from django.core.files.storage import default_storage


@csrf_exempt
@api_view(["GET"])
def get_recipes(request):
    recipes = Recipes.objects.all()
    recipe_serialized = RecipeSerializer(recipes, many=True)
    return JsonResponse(
        {"api": "CRUD MONGO", "data": recipe_serialized.data, "version": "1.0.0"},
        safe=False,
    )


@csrf_exempt
@api_view(["POST"])
def create_recipes(request):
    data = JSONParser().parse(request)
    print(data)
    recipe_serialized = RecipeSerializer(data=data)
    if recipe_serialized.is_valid(raise_exception=True):
        recipe_serialized.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse({"message": "Some Error Occured!"}, safe=False)


@csrf_exempt
@api_view(["PUT", "PATCH"])
def update_recipes(request, id):
    recipes = Recipes.objects.filter(recipe_id=id).get()
    recipe_data = JSONParser().parse(request)
    recipe_serialized = RecipeSerializer(recipes, data=recipe_data)
    if recipe_serialized.is_valid():
        recipe_serialized.save()
        return JsonResponse("Updated Successfully", safe=False)
    return JsonResponse({"message": "Some Error Occured!"}, safe=False)


@csrf_exempt
@api_view(["DELETE"])
def delete_recipes(request, id):
    recipes = Recipes.objects.filter(recipe_id=id).get()
    recipes.delete()
    return JsonResponse({"message": "Deleted Successfully"}, safe=False)


@csrf_exempt
@api_view(["GET"])
def get_chefs(request):
    chef = Chef.objects.all()
    chef_serialized = ChefSerializer(chef, many=True)
    return JsonResponse(
        {"api": "CRUD MONGO", "data": chef_serialized.data, "version": "1.0.0"},
        safe=False,
    )


@csrf_exempt
@api_view(["POST"])
def create_chef(request):
    data = JSONParser().parse(request)
    chef_serialized = ChefSerializer(data=data)
    if chef_serialized.is_valid():
        chef_serialized.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse({"message": "Some Error Occured!"}, safe=False)


@csrf_exempt
@api_view(["PUT", "PATCH"])
def update_chef(request, id):
    chef = Chef.objects.filter(recipe_id=id).get()
    chef_data = JSONParser().parse(request)
    chef_serialized = ChefSerializer(chef, data=chef_data)
    if chef_serialized.is_valid():
        chef_serialized.save()
        return JsonResponse("Updated Successfully", safe=False)
    return JsonResponse({"message": "Some Error Occured!"}, safe=False)


@csrf_exempt
@api_view(["DELETE"])
def delete_chef(request, id):
    recipes = Chef.objects.filter(recipe_id=id).get()
    recipes.delete()
    return JsonResponse({"message": "Deleted Successfully"}, safe=False)


@csrf_exempt
@api_view(["POST"])
def SaveFile(request):
    file = request.FILES["file"]
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
