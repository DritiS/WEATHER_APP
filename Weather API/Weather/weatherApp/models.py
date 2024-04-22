from django.db import models

# Create your models here.

class weather(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=10)
    coordinate = models.CharField(max_length=20)
    temperature = models.CharField(max_length=20)
    pressure = models.DecimalField(max_digits=10, decimal_places=2)
    humidity = models.DecimalField(max_digits=10, decimal_places=2)
    