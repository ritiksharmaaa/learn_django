from django.shortcuts import render
from .forms import saveform 
from django.http import HttpResponseRedirect
from . models import userdata 

# Create your views here.

def delete(request ,id ):
    print(id)
    reg = userdata(id)
    reg.delete()
    return HttpResponseRedirect('/save/form')

# def update(request , id ):
#     data= userdata.objects.get(id=id)
#     print(data.name)
#     print(data.email)
#     print(data.password)

#     form = saveform(request.POST or None)
#     if form.is_valid():
#         form.save()
        
#         context={
#         'form' : form
#          }
#     else:
#             context={
#             'form' : form
#         }
#     return render(request ,'update_home.html' ,context )



# in this save we using a function update in form which we uses .

# def update(request ,id ):
#     instance = userdata.objects.get(id=id)
#     if request.method == 'POST':
#         form = saveform(request.POST)
#         if form.is_valid():
#             form.update(instance)
#                 # instance.name = form.cleaned_data['name']
#                 # instance.email = form.cleaned_data['email']
#                 # instance.password = form.cleaned_data['password']
#                 # instance.save()
#             return HttpResponseRedirect('/save/form/')
#         else:
#             form = saveform(initial={
#             'name' : instance.name,
#             'email' : instance.email,
#             'password' : instance.password,
#         })
#     context={
#         'form' : form
#     }


#original creators .

def update(request , id ):
    instance  = userdata.objects.get(id=id)
    print(instance.password)
    if request.method == "POST":
        fm = saveform(request.POST)
        if fm.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            password  = request.POST.get('password')
            reg = userdata(id=id ,name=name , email=email , password=password )
            reg.save()
            #for delete you just give one parrameter inside instance and call id reg.delete()
            #reg = user(name=nm , email=em , password=pw) this is happen when you update 
            #reg = user(id=1) thsn reg.delete 
            # print(request.POST.get('name'))
            return HttpResponseRedirect('/save/form')
    else :
        fm = saveform(initial={'name' : instance.name , 'email' : instance.email , 'password' : instance.password })
    context={
        'form' : fm 
    }
    return render (request , 'update_home.html' , context )

def main_page(request):
    udata = userdata.objects.all()
    if request.method == "POST":
        fm = saveform(request.POST)
        if fm.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            password  = request.POST.get('password')
            reg = userdata(name=name , email=email , password=password )
            reg.save()
            #for delete you just give one parrameter inside instance and call id reg.delete()
            #reg = user(name=nm , email=em , password=pw) this is happen when you update 
            #reg = user(id=1) thsn reg.delete 
            # print(request.POST.get('name'))
            return HttpResponseRedirect('/save/form')
    else :
        fm = saveform()
    context={
        'form' : fm ,
        'data' : udata
    }
    return render(request , 'home_page.html',  context )