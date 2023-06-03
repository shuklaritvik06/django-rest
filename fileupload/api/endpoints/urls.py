from django.urls import path
from .views import FileUploadView, GridFSUploadView

urlpatterns = [
    path('', FileUploadView.as_view(), name='file-upload'),
    path('gridfs/', GridFSUploadView.as_view(), name='gridfs-upload'),
]
