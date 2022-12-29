from django.shortcuts import render
from .models import Profile
from rest_framework.response import Response
from .serealizer import ProfileSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class StudentApi(APIView):
    def get(self,request,format=None,pk=None):
        id = pk
        if id is not None:
            stu=Profile.objects.get(pk=id)

            serializer = ProfileSerializer(stu,data=request.data)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
        stu=Profile.objects.all()
        serializer = ProfileSerializer(stu,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializer=ProfileSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    def put(self,request,format=None,pk=id):
        id=pk
        stu=Profile.objects.get(pk=id)
        serializer=ProfileSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_204_NO_CONTENT)
    def patch(self,request,format=None,pk=id):
        id = pk
        stu=Profile.objects.get(pk=id)
        serializer=ProfileSerializer(stu,partial=True,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self,request,pk=id,format=None):
        id=pk
        stu=Profile.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'delete data'})

        

        
            
