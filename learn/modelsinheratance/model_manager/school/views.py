from django.shortcuts import render
from .models import Student

# Create your views here.

def home(request):
    # stu = Student.students.all()
    stu = Student.objects.all()
    context = {
        'stu' : stu 
    }
    return render (request , 'home.html' , context )
