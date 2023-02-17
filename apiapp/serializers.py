from rest_framework import serializers
from .models import Student

class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter Book Id")
    tittle=serializers.CharField(label="Enter Book Tittle")
    author=serializers.CharField(label="Enter Author Name")

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
     
