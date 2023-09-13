from django.db import models

# Create your models here.

class Post(models.Model):
    blog_title = models.CharField( max_length=100)
    blog_desc = models.CharField( max_length=500)
    publish_date = models.DateTimeField()
    


