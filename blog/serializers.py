from rest_framework import serializers
from .models import Blog

class Blogserializer (serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=["post","title","content","author","category","comment","created_at","updated_at","published_at","status"]

class BlogSerializer(serializers.Serializer):
    post= serializers.CharField ()
    title= serializers.CharField ()
    content= serializers.CharField ()
    author= serializers.CharField ()
    category= serializers.CharField ()
    comment=serializers.CharField ()
    created_at= serializers.DateTimeField ()
    updated_at= serializers.DateTimeField ()
    published_at= serializers.DateTimeField ()
    status= serializers.CharField ()
    
    def create(self,validated_data):
        return Blog.objects.create(**validated_data)