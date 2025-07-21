from .models import Register
class Registerserializer (serializers.ModelSerializer):
    class Meta:
        model=Register
        Field="__all__"
