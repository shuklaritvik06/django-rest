from django.contrib import admin
from django.urls import path, include
from .views import home_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_page),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/", include("crud.urls")),
]
