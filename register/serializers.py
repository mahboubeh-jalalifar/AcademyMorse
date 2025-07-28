from rest_framework import serializers
from .models import Register


class Registerserializer (serializers.ModelSerializer):
    class Meta:
        model=Register
        Field=["frist_name","last_name","password","age","birthday","email","phonenumber","adress","created","role"]

class RegisterSerializer(serializers.serializer):
    first_name= serializers.CharField (max_length=0)
    last_name= serializers.CharField (max_length=50)
    password= serializers.CharField (max_length=50)
    age= serializers.IntegerField ()
    birthday= serializers.DateField ()
    email= serializers.EmailField (unique=True)
    phonenumber= serializers.IntegerField (max_length=15 , unique=True)
    adress= serializers.CharField ()
    created= serializers.DateField ()
    role= serializers.CharField (max_length=10, default="User", choices="ROLE_CHOICES")

    def create (self,validated_data):
        return Register.objects.create(**validated_data)