from django.shortcuts import render
from .forms import studentForm , stuform , teacherform 
from django.http import HttpResponseRedirect
from .models import student


# Create your views here.


def update_page(request , id):
    instancec = student.objects.get(id=id)

    

    if request.method == 'POST':
        fm = studentForm(request.POST , instance=instancec)
        if fm.is_valid():
            nm = request.POST.get('name')
            em = request.POST.get('email')
            ps = request.POST.get('password')
            # print(request.POST.get('name'))
            reg = student( id=id ,name=nm , email=em , password=ps)
            reg.save()
            return HttpResponseRedirect('/model/form')
    else:
        fm = studentForm(instance=instancec)
    context={
        'form':fm
    }
    return render(request , 'update_modelform.html' ,context)


def page_delete(request,id):
    fm = student.objects.get(id=id)
    print(fm)
    fm.delete()
    return HttpResponseRedirect('/model/form/')


def mform_page(request):
    udata = student.objects.all()
    

    if request.method == 'POST':
        fm = studentForm(request.POST)
        if fm.is_valid():
            nm = request.POST.get('name')
            em = request.POST.get('email')
            ps = request.POST.get('password')
            # print(request.POST.get('name'))
            reg = student(name=nm , email=em , password=ps)
            reg.save()
            return HttpResponseRedirect('/model/form')
    else:
        fm = studentForm()
    context={
        'form':fm,
        'data' : udata,
    }
    return render(request , 'modelform.html' ,context)


# model form inheritance 

def forminherit(request):
    stu  = stuform()
    teacher = teacherform()
    context = {
        'stu': stu ,
        'teacher' : teacher 
    }
    return render(request , 'modelinheritance.html' , context )
