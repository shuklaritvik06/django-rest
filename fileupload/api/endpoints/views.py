from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from .models import File
from django.conf import settings
from gridfs import GridFS


class FileUploadView(APIView):
    
    def get(self, request, *args, **kwargs):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        File.objects.create(file=file)
        return Response(status=status.HTTP_201_CREATED)
    
    
class GridFSUploadView(APIView):
   def __init__(self):
         self.fs = GridFS(settings.DB, collection='uploads')
   def get(self, request, *args, **kwargs):
       files = File.objects.all()
       serializer = FileSerializer(files, many=True)
       return Response(serializer.data)
   
   def post(self, request, *args, **kwargs):
       file_id = self.fs.put(request.FILES.get('file'), filename=request.FILES.get('file').name)
       return Response(str(file_id), status=status.HTTP_201_CREATED)