from django.shortcuts import render
from .forms import argsform

# Create your views here.

def f_args(request):
    fm = argsform()
    context={
        'form' : fm
    }
    return render (request , "f_args.html" , context )