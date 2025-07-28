from django.db import models

class Accounting(models.Model):
    user=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    def __str__(self):
        return (f"{self.user}")