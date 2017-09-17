from django.db import models

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
