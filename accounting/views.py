from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Accounting
from serializers import AccountingSerializer

def say_hello(request):
    return HttpResponse ("Hello")

class AccountingCreateView (APIView):
    def get(self,request):
        accounting=Accounting.objects.all ()
        serializer=AccountingSerializer(accounting,many=True)
        return Response (serializer.data)
    def post (self,request):
        serializer=AccountingSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_200_OK)
        return Response (serializer.data, status=status.HTTP_204_NO_CONTENT)

class AccountingSerializerview(generics.ListCreateAPIView):
    queryset=Accounting.objects.all()
    serializer_class=AccountingSerializer

 
    
