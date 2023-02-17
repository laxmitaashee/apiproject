from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

from rest_framework import viewsets


class BookApiView(APIView):
    serializer_class=BookSerializer
    def get(self,request):
        allBooks=Book.objects.all().values()
        return Response({"Message":"List of Books","Book list":allBooks})
    
    def post(self,request):
        print("Request data is:",request.data)
        serializer_obj=BookSerializer(data=request.data)
        if(serializer_obj.is_valid()):
            Book.objects.create(id=serializer_obj.data.get("id"),
                            tittle=serializer_obj.data.get("tittle"),
                            author=serializer_obj.data.get("author"))
        book=Book.objects.filter(id=request.data["id"]).values()
        return Response({"Message":"New book added!","Book":book})
    

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    
    


