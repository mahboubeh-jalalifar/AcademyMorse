from time import timezone
from django.db import models
from django.forms import CharField, EmailField

class Register(models.Model):
    first_name= models.CharField (max_length=50)
    last_name= models.CharField (max_length=50)
    password= models.CharField (max_length=50)
    age= models.IntegerField ()
    birthday= models.DateField ()
    email= models.EmailField (unique=True)
    phonenumber= models.IntegerField (max_length=15 , unique=True)
    adress= models.CharField ()
    created= models.DateField (default=timezone)
    role= models.CharField (max_length=10, default="User", choices="ROLE_CHOICES")
    gender= models.CharField (max_length= 10, default="Other", choices="GENDER_CHOICES")
    def __str__ (self):
        return f"{self.first_name} {self.last_name} {self.password}{self.age}{self.birthday}{self.email}{self.phonenumber}{self.adress}{self.created}{self.role}{self.gender} "

class Register (models.Model):
    ROLE_CHOICES=[
        ("A","Admin"),
        ("U","User")
                  ]

    GENDER_CHOICES= [
        ("M","male"),
        ("F","Female"),
        ("O","Other")
                 ]