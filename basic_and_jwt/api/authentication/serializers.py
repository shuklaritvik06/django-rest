from rest_framework.serializers import ModelSerializer, CharField
from .models import User
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token


class RegisterSerializer(ModelSerializer):
    email = CharField(max_length=100)
    username = CharField(max_length=45)
    password = CharField(min_length=8, write_only=True)
    
    
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"])
        if email_exists:
            raise ValidationError("Email Already been used!")
        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
