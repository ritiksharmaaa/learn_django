from django.shortcuts import render
from .models import  Teacher ,School 
from django.db.models import Q 

# Create your views here.
def student(request):
    # stu = School.objects.all()

    # stu = School.objects.filter(marks=345)
    # stu = School.objects.exclude(marks=345)
    # stu = School.objects.order_by('marks') # use marks /name / roll / city / date for asc 
    # stu = School.objects.order_by('-marks') # use marks for desc
    # stu = School.objects.order_by('?') # use '?' for desc
    # stu = School.objects.order_by('id').reverse() # do to check reverse .and
    # stu = School.objects.order_by('id').reverse()[:5] #  reverse with slicing method 
    # stu = School.objects.values() # without parameter it return all value in dict not list . 
    # stu = School.objects.values('name' , 'roll') # with parameter 
    # stu = School.objects.values_list() # this is similar to value but it wrap all date in tuple 

    # stu = School.objects.values_list( 'id' , 'name' ) # with parameters same waht field need write this  but it not show inside template becaue named = false we need to true but data extract but only used in python not frontend side 
    # stu = School.objects.values_list('id' , 'name' , named=True ) ro associate data with there labels 
    # stu = School.objects.using('default')# use when no obout you datbase .
    # stu = School.objects.dates('pass_date' , 'month')# mean can canhelp to find disting value like name , year day , mean one data for each type of fileds shows not dublicate .
    # stu = School.object

    # ====================================================second table "teacher" Started =================================

    # qs1 = School.objects.values_list('id' , 'name' , named=True) # all =True for if want dublicate values .
    # qs2 = Teacher.objects.values_list('id' , 'name' , named=True)
    # stu = qs2.union(qs1) # it give all name of teacher and student but the name is twice show as once distint value are provide 
    
    
    
    # ======================Intersection =================================

    
    # qs1 = School.objects.values_list('id' , 'name' , named=True) # all =True for if want dublicate values .
    # qs2 = Teacher.objects.values_list('id' , 'name' , named=True)
    # stu = qs2.intersection(qs1)
    
    
    
    # =====================================difference===========================

    
    # qs1 = School.objects.values_list('id' , 'name' , named=True) # all =True for if want dublicate values .
    # qs2 = Teacher.objects.values_list('id' , 'name' , named=True)
    # stu = qs2.difference(qs1)


    # =================================operators ============================================
    # stu = School.objects.filter(id=1) & School.objects.filter(roll=51153568)
    # stu = School.objects.filter(id=1 , roll=51153568)
    
    # stu = School.objects.filter(Q(id=1 ) & Q(roll=51153568))
    stu = School.objects.filter(Q(id=1 ) | Q(roll=51153568))


    print('checking what inside the objecst ' , stu)
    print("-------------------------------------------------")
    # checking which sql query run how it happen 
    print("Sql" , stu.query)
    context ={
        'students' : stu
    }
    return render(request , 'student.html ' , context )
