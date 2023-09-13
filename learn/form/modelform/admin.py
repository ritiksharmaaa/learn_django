from django.contrib import admin
from . models import student , modelinheritance

# Register your models here.
@admin.register(student)
class userdataAdmin(admin.ModelAdmin):
    list_display = ( 'id' , 'name' ,'email' , 'password' )

    
@admin.register(modelinheritance)
class userdataAdmin(admin.ModelAdmin):
    list_display = ( 'id' , 'student_name' , 'teacher_name' ,  'email' , 'password' )

