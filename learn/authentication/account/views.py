from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages 
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm , SetPasswordForm
from django.contrib.auth import authenticate , login , logout , update_session_auth_hash
from .forms import signup


# authhenticate these check wheatehr user and pass afe correct or not if not it retun none 
# Create your views here.


def sing_up(request):
    if request.method == "POST":
        fm = signup(request.POST)
        if fm.is_valid():
            messages.success(request,"User Registration Succesfully")
            print(request.POST.get('username'))
            fuser = m.save()
            group = Groups.objects.get(name="hi") # hi is a group 
            user.groups.add(group) # this will do dynamic to diffrent diffrent permision 

            return HttpResponseRedirect('/')
    else: 
         fm = signup()
    context={
        'form' : fm 
    }
    return render(request ,'signup.html' ,  context )



# We want both fields in form because in this form in this form we have only the password and confirm password but if we wanted tosome more field in the form so what we have to do we have to create a forms that we and and from the model we can make our own models form so we can get more fields 


# def sing_up(request):
#     if request.method == "POST":
#         fm = UserCreationForm(request.POST)
#         if fm.is_valid():
#             print(request.POST.get('username'))
#             fm.save()
#     else: 
#          fm = UserCreationForm()
#     context={
#         'form' : fm 
#     }
#     return render(request ,'signup.html' ,  context )


#-------------------------------------login views -----------------------------------


def log_in(request):
    # made one more if user is alredy login not show this user . 
    if request.method == "POST":
        fm = AuthenticationForm(request=request , data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            # uname = request.POST.get('username')
            # upass = request.POST.get('password')
            user = authenticate(username=uname , password=upass)
           
            # print (user , uname , upass )
            if user is not None :
                login(request , user)
            
                messages.success(request ,f"{user} login sussecfully !" )
                return HttpResponseRedirect('/')
    else:
        fm = AuthenticationForm()
    context={
        'form' : fm ,
    }
    return render(request , 'userlogin.html' , context )



    #- --- we have to make a userprofile there but it ok to have seperate file . 

    # logout view  

def log_out(request):
    logout(request)
    messages.success(request , 'Logout successfully')
    return HttpResponseRedirect('/')




#-------------------- password change form using old password -------------------- 

def password_change(request):
    # make sure you have check user is authenticated that it change other wise any one can access via url banner text paste 
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user , data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request , fm.user)
                messages.success(request , "password changed succefully ")
                return HttpResponseRedirect('/')
    else:
        return  HttpResponseRedirect('/')
    fm = PasswordChangeForm(user = request.user )
    context = {
        'form' : fm 
    }
    return render(request , 'passwordchange.html' , context )


#---------------------- password change form directly --------------------------------

def password2_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user , data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request , fm.user )
                messages.success(request , 'password change succefully')
                return HttpResponseRedirect("/")
    
    else:
        return HttpResponseRedirect('/')
    fm = SetPasswordForm(user=request.user)
    context = {
            'form' : fm ,
        }
    return render(request , 'password2change.html' ,context )


# ================= making tjis view to check whetehet  permission happen or not . 


def dashboard(request):
    if request.user.is_authenticated:

        return render(request , 'permdashboard.html' , {'user' : request.user})
    else:
        return HttpResponseRedirect('/login/')