from statistics import mode
from django.db import models

# Create your models here.
class User(models.Model):
    userName : models.CharField(max_length=100)
    passwordHash : models.CharField(max_length=256)