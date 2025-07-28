from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from register.models import Register
from .serializers import RegisterSerializer

def show_name (request):
    first_name="Mahboubeh"
    last_name="Jalalifar"
    return HttpResponse({f"Name:{first_name}<br>Lastname:{last_name}"})

class RegisterCreateView(APIView):
    def get (self,request):
        register=Register.objects.all()
        serializer=RegisterSerializer(register,many=True)
        return Response(serializer.data)
    def post (self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
    
class RegisterCreateView(generics.ListCreateAPIView):
    queryset=Register.objects.all()
    serializer_class=RegisterSerializer