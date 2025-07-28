from rest_framework import serializers
from .models import Accounting

class AccountingSerializer (serializers.Modelserializer):
    class meta:
        model=Accounting
        Field=["user","email"]

class AccountingSerializer (serializers.serializer):
    user=serializers.CharField (max_weight=50)
    email=serializers.EmailField()

    def create(self,validated_data):
        return Accounting.objects.create(**validated_data)
    

