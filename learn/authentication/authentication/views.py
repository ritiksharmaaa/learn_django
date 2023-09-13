
from django.shortcuts import render 
from django.http import HttpResponseRedirect 
from django.contrib import messages 
# from django.contrib.auth.forms import UserChangeForm
from account.forms import userProfile


def home_page(request):
    return render(request , 'index.html')

def profile_page(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = userProfile(request.POST , instance=request.user)
            if fm.is_valid():
                messages.success(request ,"user profile updated ! ")
                fm.save()
                return HttpResponseRedirect('/')
        #we want own custom form so we can make own using inherit userchange form 
        fm = userProfile(instance=request.user)
        name = request.user
        return render(request , 'profile.html' , {'user' : name  , 'form': fm})
    else :
         return HttpResponseRedirect('/singin/')