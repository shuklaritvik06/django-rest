from rest_framework import serializers
from crud.models import Books, Authors


class BookSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Books
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Authors
        fields = "__all__"
