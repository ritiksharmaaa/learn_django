from django.db import models
# from django.db.manager.Manager import Manager  
from .manager import CustomManager
# Create your models here.

class Student(models.Model):
    name = models.CharField( max_length=50)
    roll_in_words = models.CharField( max_length=100)
    students = CustomManager()
    # students = models.Manager() # this way chanfe objects into your custom name .
    objects  = models.Manager()
