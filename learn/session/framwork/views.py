from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'ritik' # and same alos use for update 
    return render(request ,'set_session.html')

def getsession(request):
    name =  request.session['name']
    print(name)
    return render(request , 'get_session.html' , {'name': name })

def delsession(request):
    request.session.flush()
    return render(request ,'del_session.html')