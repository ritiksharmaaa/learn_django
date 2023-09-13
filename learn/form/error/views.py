from django.shortcuts import render
from .forms import styile ,styile2 

# Create your views here.
def error_page(request):
    if request.method == "POST":
        fm = styile(request.POST)
        if fm.is_valid():
            print(request.POST.get('name'))
    else :
        fm  =  styile()
    context = {}
    context['form']=fm
    return render (request , 'error.html' ,context)





def error_page2(request):
    if request.method == "POST":
        fm = styile2(request.POST)
        if fm.is_valid():
            print(request.POST.get('name'))
    else :
        fm  =  styile2()
    context = {}
    context['form']=fm
    return render (request , 'error2.html' ,context)