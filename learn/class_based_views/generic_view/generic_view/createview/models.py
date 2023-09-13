from django.db import models
from django.urls import reverse

# Create your models here.
class createview_student(models.Model):
    name =  models.CharField(("name"), max_length=50) # here name inside () - are show in admin .
    email = models.EmailField(("email"), max_length=254)
    password = models.CharField(("password"), max_length=50)


    def get_absolute_url(self):
        return reverse("fromViewthankyou") # here the string is name of actual url where it return . 
    