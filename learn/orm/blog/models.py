from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class blog(models.Model):
    blog_title = models.CharField( max_length=50)
    blog_desc = models.CharField(max_length=500)
    blog_like = models.IntegerField()
    create_by = models.EmailField( max_length=34)

    def __str__(self):
        return str(self.id)


# mant to one filed ------------
# use of foreigh keyrwquire two args first class second oncascade


''' just like a father has 3 child same as . mean father is one but children is to many . 
real time examp - is user id is 1 - it can post to many contetnt but the id is belongs to user 1 '''


    

   
    

class post (models.Model):

   user =  models.ForeignKey(User , on_delete=models.CASCADE)
   post_title = models.CharField( max_length=50)
   post_cat = models.CharField(max_length=50)
   post_publish_date = models.DateField()


   def __str__(self):
       return self.post_title





# many to many fields 

class authore(models.Model):
    authore_name = models.CharField( max_length=50)
    authore_desc = models.CharField( max_length=50)   


    def __str__(self):
        return self.authore_name




class book(models.Model):
    btitle = models.CharField( max_length=50)
    bdesc = models.CharField( max_length=50)
    bauthore = models.ManyToManyField(authore)
    

    def writen_by(self):
        return ",".join([str(p) for p in self.bauthore.all()])


class Vehicle(models.Model):
    reg_no = models.IntegerField()
    owner = models.CharField(max_length = 100)

    def __str__(self):
        return self.owner
    
  
class Car(models.Model):
    vehicle = models.OneToOneField(Vehicle, 
          on_delete = models.CASCADE, primary_key = True)
    car_model = models.CharField(max_length = 100)



    def own_by(self):
        return self.vehicle


    


    