from rest_framework.generics import GenericAPIView
from .serializers import RegisterSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.forms.models import model_to_dict
from .tokens import create_jwt_pair_for_user
from rest_framework.decorators import api_view


@api_view(["GET"])
def home_page(request):
    return JsonResponse({
        "message": "API is up!"
    })

class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = []
    def post(self, request):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({
                "api_version":"1.0.0",
                "message": "User Created Successfully!",
                "data": serialized_data.data
            })
        return JsonResponse({
            "message": serialized_data.errors
        })
            
class LoginView(GenericAPIView):
    permission_classes = []

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        user = authenticate(email=email, password=password)
        tokens = create_jwt_pair_for_user(user=user)
        if user is not None:
            return JsonResponse({
                "message": {
                    "authenticated": True,
                    "auth_token": tokens
                }
            })
        return JsonResponse({
            
        })