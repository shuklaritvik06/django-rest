from rest_framework import viewsets
from crud.models import Books, Authors
from crud.serializers import BookSerializer, AuthorSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=["get"])
    def authors(self, request, pk=None):
        try:
            book = Books.objects.get(pk=pk)
            author = Authors.objects.filter(books=book)
            authors = AuthorSerializer(author, many=True, context={"request": request})
            return Response(authors.data)
        except Exception as e:
            return Response({"message": "Book ID is wrong"})


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer
