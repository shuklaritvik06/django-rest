from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    create_chef,
    create_recipes,
    delete_chef,
    delete_recipes,
    update_chef,
    update_recipes,
    get_chefs,
    get_recipes,
    SaveFile,
)

urlpatterns = [
    path("recipes/", get_recipes),
    path("chefs/", get_chefs),
    path("recipes/create/", create_recipes),
    path("recipes/update/<uuid:id>", update_recipes),
    path("recipes/delete/<uuid:id>", delete_recipes),
    path("chefs/create/", create_chef),
    path("chefs/update/<uuid:id>", update_chef),
    path("chefs/delete/<uuid:id>", delete_chef),
    path("file/", SaveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
