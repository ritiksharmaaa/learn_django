from django.db import models
from django.contrib.auth.models import User 



# Create your models here.
class Page(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE ,primary_key=True)# limit_choices_to={'is_staff' : True}
    page_name = models.CharField( max_length=70)
    page_cat = models.CharField( max_length=50)
    page_publish_date = models.DateField()
    
    # code copy : Just because we have to make a new project where these upper model we need and the next model we will write it so we wanted to make the project in a single product so that's why we are not making another project which is write the next code so upper code isin a first topic.abs
class Like(Page):
    # model inheritance 
    panna = models.OneToOneField(User , on_delete=models.CASCADE ,primary_key=True , parent_link=True)#this code is page to change the sequel name field it because the like ID is written like page _PTR _it which is not scored so what we do if we wanted to game own custom name so that's why we are pasting thiscode to change the name called Panna.
    likes = models.IntegerField()
    # In this we are defining model in entrance so it is just like making a lesson one to one with page model

   





















