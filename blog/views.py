from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import pytz
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Blog
from .serializers import BlogSerializer

def Iran_time(request):
    Iran_timezone= pytz.timezone("Asia/Tehran")
    now=datetime.now (Iran_timezone)
    current_time=now.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse (f"Today is: {current_time}")

class BlogCreateView(APIView):
    def get (self, request):
        blog=Blog.objects.all()
        serializer=BlogSerializer(blog,many=True)
        return Response(serializer.data)
    def post (self, request):
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response (serializer.data,status=status.HTTP_204_NO_CONTENT)

class BlogSerializerView(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

