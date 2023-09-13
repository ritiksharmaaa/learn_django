from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from . forms import reg_form

# Create your views here.
def user_registration(request):
    if request.method == "POST":
        fm = reg_form(request.POST)
        if fm.is_valid():
            fm.save()
            messages.info(request , "now you can log in !")
            # print(messages.get_level(request)) output is 20 which is code of this info 
            messages.debug(request , "this is old ")
            messages.set_level(request , messages.DEBUG) #mean no wan see lower than  that code only higer val only 
            messages.debug(request , "this is new debug  ")
            print(messages.get_level(request))
            
            # messages.add_message(request , messages.SUCCESS , 'Your Account Has Been Created ! ')
    else : 
        fm = reg_form()   
    fm = reg_form()
    context={
        'form' : fm 
    }
    return render(request , 'userregister.html' , context )
