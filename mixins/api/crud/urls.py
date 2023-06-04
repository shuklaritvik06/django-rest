from django.urls import path
from .views import BooksView, UpdateDeleteView

urlpatterns = [
    path("books/", BooksView.as_view(), name="books-view"),
    path("books/change/<int:book_id>", UpdateDeleteView.as_view(), name="books-change")
]
