from django.db import models

# Create your models here.)

class student(models.Model):
    name = models.CharField( max_length=70)
    email = models.EmailField( max_length=254 , blank=True)
    password = models.CharField(max_length=50)



class modelinheritance(models.Model):
    student_name = models.CharField( max_length=70)
    teacher_name = models.CharField( max_length=100)
    email = models.EmailField( max_length=254 , blank=True)
    password = models.CharField(max_length=50)