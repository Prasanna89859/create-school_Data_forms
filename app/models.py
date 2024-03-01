from django.db import models
from app.models import *

# Create your models here.

class Student(models.Model):
    Sname=models.CharField(max_length=100)
    Sage=models.IntegerField()
    Smobile=models.CharField(max_length=10)
    def __str__(self):
        return self.Sname
