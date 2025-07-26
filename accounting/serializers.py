from django.core import serializers
from .models import Accounting

class Accountserializer (serializers.Modelserializer):
    class meta:
        model=Accounting
        Field="__all__"
