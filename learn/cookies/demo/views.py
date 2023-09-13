from django.shortcuts import render
from datetime import datetime , timedelta


# Create your views here.

def seting(request): # there the request came 
    response = render(request , 'set.html')
    # response.set_cookie('name' , 'ritik' ,max_age=60)
    # response.set_cookie('iname' , 'ritik' ,expires=datetime.utcnow()+timedelta(days=2))
    response.set_signed_cookie('pname' , 'pkey' , salt='nm' ,expires=datetime.utcnow()+timedelta(days=2))
    return response 

#    return render (request , 'set.html') # we give response but not direct give response we store in var than set cookies .


def getting(request):
    try:
        #we can also use .get and give default value .  method to secure code fail error . 
        # c = request.COOKIES['name']
        c = request.get_signed_cookie('pname' , salt="nm") # so when ever server set cookie it also set hash  type val in user clinet , and next time when any user want to forcefully access this cookie they nedd to provide to getting cookie than it get by server . 
    except :
        c = "no cookies "
    return render(request , 'get.html' , {'k' : c})

def deleting(request):
    


    response =  render(request , 'del.html')
    response.delete_cookie('name')
    return response 