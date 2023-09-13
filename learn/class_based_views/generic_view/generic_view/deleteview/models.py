from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(("name"), max_length=50)
    email = models.EmailField(("email"))
    password = models.CharField(("passwordcls"), max_length=50)
