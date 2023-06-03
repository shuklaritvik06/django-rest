from django.urls import path, include
from crud.views import BookViewSet, AuthorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r"author", AuthorViewSet)


urlpatterns = [path("", include(router.urls))]
