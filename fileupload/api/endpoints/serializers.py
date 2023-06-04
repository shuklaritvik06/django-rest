from rest_framework.serializers import ModelSerializer
from .models import File

class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = [
            "file"
        ]
    
    def validate(self, data):
        file = data.get('file')
        if file.size > 1024*1024*2:
            raise serializers.ValidationError("File size should not exceed 2 MB")
        return data    

    def create(self, validated_data):
        file = File.objects.create(**validated_data)
        return file
    
    
        