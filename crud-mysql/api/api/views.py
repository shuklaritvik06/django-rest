from django.http import JsonResponse
from rest_framework.decorators import api_view


def home_page(request):
    return JsonResponse(
        {
            "status": "OK",
            "author": "Ritvik Shukla",
            "apiVersion": "1.0.0",
            "description": "A book CRUD (Create, Retrieve, Update, Delete) API in Django Rest Framework (DRF) allows users to perform various operations on book data through a RESTful interface.",
        },
        safe=False,
    )
