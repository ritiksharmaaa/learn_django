from django.db import models

# Create your models here.

class baseinfo(models.Model):
    name = models.CharField( max_length=50)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract=True

class Student(baseinfo):
    fess = models.IntegerField()
    date = None # when yiu dont want to inherit some specific fields 

class Teacher(baseinfo):
    salary = models.IntegerField()

class contractor(baseinfo):
    payment = models.IntegerField()


#-------------------------------multitable inheratance ------------------------------------

class Examcenter(models.Model):
    cname = models.CharField( max_length=50)
    city = models.CharField( max_length=50)
    
class mstudent(Examcenter):
    name = models.CharField( max_length=50)
    roll = models.IntegerField()


#-------------------------------------proxy-------------------------models --------

# we perform  all operation in above models .

class Examcenters(models.Model):
    cname = models.CharField( max_length=50)
    city = models.CharField( max_length=50)

class MyExamCenter(Examcenters):
    class Meta:
        proxy = True 
        ordering = ['-id'] # mean in your admin pannel data show 4321 wise so change to 1234 wise 