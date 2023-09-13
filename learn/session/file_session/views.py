from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def set(request):
    request.session['name'] = 'Ritik'
    return render(request , 'set_session.html')

def get(request):
    if 'name' in request.session:
        name  =  request.session['name']
        request.session.modified = True
        return render(request , 'get_session.html' ,{'name':name })
    else:
        return HttpResponse("session expire")


def dt(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request , 'del_session.html')
