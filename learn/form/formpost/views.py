from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import fpost 

# Create your views here.


def thankyou(request):
    return render(request , 'success.html')


def formpost(request):
    if request.method == 'POST':
        fm  = fpost(request.POST)
        # print(fm , 'check form request post ')
        if fm.is_valid():
            print("form is validate ! ")
            # print(fm.cleaned_data.get('name')) we can acces this element like this 

            name = request.POST.get('name')
            email = fm.cleaned_data.get('email')
            password = fm.cleaned_data.get('password')


            context= {}
            context['name'] = name 
            context['email'] = email 
            context['password'] = password 
            return HttpResponseRedirect('/thankyou')
            # we wuse redirest method to can specfic view function so we can use 
            # return render(request , 'success.html' , context  it take views base callable function .
    else:
       fm = fpost()
       context = {}
       context['form'] = fm
    return render(request , 'formpost.html'  , context)