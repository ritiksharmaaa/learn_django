from django.shortcuts import render
from .models import Student
from datetime import date , time
# Create your views here.

def home (request):
    # stu = Student.objects.all()
    # stu = Student.objects.filter(marks__gt=900)
    # stu = Student.objects.filter(marks__lt=700)
    # stu = Student.objects.filter(name__iexact='ritik sharma')
    # stu = Student.objects.filter(name__iexact='ritik sharma')
    # stu = Student.objects.filter(marks__gte=765)
    # stu = Student.objects.filter(marks__lte=765)
    # stu = Student.objects.filter(name__startswith='nik')
    # stu = Student.objects.filter(name__istartswith='rit')
    # stu = Student.objects.filter(name__endswith='ika')
    # stu = Student.objects.filter(name__iendswith='Hu')
    # stu = Student.objects.filter(marks__range=(400 , 600)) with date 
    # stu = Student.objects.filter(name__icontains='iti')
    # stu = Student.objects.filter(name__contains='iti')
    # stu = Student.objects.filter(id__in=[1, 6 , 8])
    # using datatime llokup first import it -------------------------------------------------
    # stu = Student.objects.filter(admdatetime__date__gt=date(2023 ,7 ,12))
    # stu = Student.objects.filter(admdatetime__date=date(2023 ,7 ,12))
    # stu = Student.objects.filter(admdatetime__date__gt=date(2020 , 6 ,5))
    # stu =Student.objects.filter(admdatetime__year=2018)
    # stu =Student.objects.filter(admdatetime__year__gte=2018)
    # stu =Student.objects.filter(admdatetime__month=4) # for is aprill 
    # stu =Student.objects.filter(admdatetime__month__gte=4)
    # stu =Student.objects.filter(admdatetime__day__gt=8)
    # stu =Student.objects.filter(passdate__week=4)
    # stu =Student.objects.filter(passdate__week__gt=4)
    # stu =Student.objects.filter(passdate__week_day=4)
    # stu =Student.objects.filter(passdate__week_day__gt=4)
    # stu =Student.objects.filter(admdatetime__time__gt=time(6,00)) # data which came after (21 ,17) 21 bajke 17 miniutes .
    # stu =Student.objects.filter(admdatetime__hour__gt=5)
    # stu =Student.objects.filter(admdatetime__minute__gt=5) # go up 60 minutes in hour 0 to 23 max val
    # stu =Student.objects.filter(admdatetime__seconds__gt=5)
    stu = Student.objects.filter(roll__isnull=True) 
     
    




    print('SQL QUERY : _ ', stu.query)
    context={
        'stu' : stu 
    }
    return render (request , 'home.html' , context )
