from rest_framework import serializers
from .models import Register


class RegisterSerializer (serializers.ModelSerializer):
    class Meta:
        model=Register
        Fields=["frist_name","last_name","password","age","birthday","email","phonenumber","adress","created","role"]

class RegisterSerializer (serializers.Serializer):
    first_name= serializers.CharField ()
    last_name= serializers.CharField ()
    password= serializers.CharField ()
    age= serializers.IntegerField ()
    birthday= serializers.DateField ()
    email= serializers.EmailField ()
    phonenumber= serializers.IntegerField ()
    adress= serializers.CharField ()
    created= serializers.DateField ()
    role= serializers.CharField ()

    def create (self,validated_data):
        return Register.objects.create(**validated_data)