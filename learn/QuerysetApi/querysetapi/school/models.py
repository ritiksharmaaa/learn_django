from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField( max_length=50)
    roll = models.CharField( max_length=50 , unique=True , null=False)
    city = models.CharField( max_length=70)
    marks = models.IntegerField()
    pass_date = models.DateField()

# creating a model to see how union queryset use . 


class Teacher(models.Model):
    name = models.CharField( max_length=50)
    empnum = models.IntegerField(unique=True , null=False)
    city = models.CharField( max_length=70)
    salary = models.IntegerField()
    join_date = models.DateField()
    