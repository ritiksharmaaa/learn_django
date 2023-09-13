from django.shortcuts import render
from .models import Student , Teacher , contractor 

# Create your views here.
def home(request):
    stu = Student.objects.all()
    tea = Teacher.objects.all()
    con = contractor.objects.all()

    context = {
        'stu' : stu ,
        'tea': tea,
        'con' : con 
    }

    return render(request , 'home.html' ,context)


def proxy(request):
    stu = Student.objects.all()
    tea = Teacher.objects.all()
    con = contractor.objects.all()

    context = {
        'stu' : stu ,
        'tea': tea,
        'con' : con 
    }

    return render(request , 'proxy.html' ,context)