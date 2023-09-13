from django.shortcuts import render
from datetime import datetime

# learning django templates language 
# Create your views here.


def lang(request):
    context ={
        'name' : 'django prasad ',
        'duration' : '4 months ',
        'seats' : 10 ,
        'bool' : False,
        'newname' : 'we have so many words',
        'datetime' : datetime.now()
    }
    return render (request , 'dtl.html' , context)

