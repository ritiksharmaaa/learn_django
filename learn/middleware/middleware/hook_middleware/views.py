from django.shortcuts import render , HttpResponse
from django.template.response import TemplateResponse 

# Create your views here.

def home(request):
    return HttpResponse('i am  home views workiong ')

def exc_home(request):
    print (" exception views ............")
    a = 10/0
    return HttpResponse('i am exce- home views workiong ')

def user_info(request):
    # here you dont want to use render methods . 
    print("I am user view.")
    context = {
        'name' : 'rahul',

    }
    return TemplateResponse('i am  home views workiong ', context )