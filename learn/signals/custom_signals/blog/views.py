from django.shortcuts import render ,HttpResponse 
from blog import signals

# Create your views here.

def home(request) : 
    signals.notification.send(sender=None , request=request , user=['geek' , 'show '])
    return HttpResponse(" this is home page ")
