from django.core import serializers
from .models import Blog
class Blogserializer (serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields="__all__"