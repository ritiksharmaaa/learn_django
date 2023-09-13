from django.shortcuts import render
from savedata.models import userdata 

# Create your views here.
def dpage(request):
    data = userdata.objects.all()
    context = {
        'data' : data 
    }
    return render(request , 'durl.html' , context )

def blog(request , name ):
    context={
        'data' : name
    }
    return render(request , 'urldynamic.html',  context)
