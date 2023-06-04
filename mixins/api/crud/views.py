from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin,RetrieveModelMixin,UpdateModelMixin
from .models import Books
from rest_framework.generics import GenericAPIView
from .serializers import BookSerializer

class BooksView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UpdateDeleteView(GenericAPIView, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'book_id'
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)    
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)