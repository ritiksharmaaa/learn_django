from django.contrib import admin
from .models import Teacher , Student ,contractor , Examcenter , mstudent , Examcenters , MyExamCenter

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display= ['name' , 'id' , 'age' , 'fess']
    

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
    

@admin.register(contractor)
class contractorAdmin(admin.ModelAdmin):
    pass

@admin.register(Examcenter)
class ExamcenterAdmin(admin.ModelAdmin):
    pass

@admin.register(mstudent)
class mstudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Examcenters)
class ExamcentersAdmin(admin.ModelAdmin):
    pass

@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    pass 


    

    

    

