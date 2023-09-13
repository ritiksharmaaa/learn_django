from django.shortcuts import render
from .models import Student
from datetime import date , time
from django.db.models import Avg , Sum ,Min , Max , Count,  Q
# Create your views here.

def home (request):
    stu = Student.objects.all()
    # stu = Student.objects.all().aggregate(Avg('marks'))
    # avg = stu.aggregate(Avg('marks'))  you can get ouptut in template also /
    #same as all function works 
    print(stu)




    context={
        'stu' : stu 
    }
    return render (request , 'home.html' , context )




def q(request):
    # stu = Student.objects.filter(Q(id=5) & Q(roll=107))
    # stu = Student.objects.filter(Q(id=5) | Q(roll=103))
    stu = Student.objects.filter(~Q(id=5))
    print(stu)
    #--------------------------implement--- Q objects -------------------------


    

    context={
        'stu' : stu 
    }
    return render (request , 'q.html' , context )


#-----------------limiting queryset -------------------------------



def limit(request):
    # stu = Student.objects.all()[:5]
    # stu = Student.objects.all()[4:7]
    stu = Student.objects.all()[:8:2]

    

    context={
        'stu' : stu 
    }
    return render (request , 'limit.html' , context )