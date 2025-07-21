from datetime import timezone
from django.db import models
from django.contrib.auth.models import User 
class Blog(models.Model):
    post= models.CharField ()
    title= models.CharField (max_length=80)
    content= models.TextField (max_length=200)
    author= models.ForeignKey (User, on_delete=models.CASCADE)
    category= models.CharField (max_length= 20)
    comment=models.CharField ()
    created_at= models.DateTimeField (auto_now_add=True)
    updated_at= models.DateTimeField (auto_now=True)
    published_at= models.DateTimeField (default=timezone)
    status= models.CharField (choices="STATUS_CHOICES", default="Published")
    def __str__(self):
        return f"{self.title}{self.author}{self.updated_at}"
    
class Blog(models.Model):
    STATUS_CHOICES=[("Published","Published"),
                    ("Draft","Draft")]

class User (models.Model):
    name=models.CharField (max_length=20)

# Create your models here.
