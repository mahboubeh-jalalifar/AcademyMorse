from rest_framework import serializers
from .models import Accounting

class AccountingSerializer(serializers.ModelSerializer):
    class meta:
        model=Accounting
        Fields=["user","email"]

class AccountingSerializer(serializers.Serializer):
    user=serializers.CharField (max_weight=50)
    email=serializers.EmailField()

    def create(self,validated_data):
        return Accounting.objects.create(**validated_data)
    

