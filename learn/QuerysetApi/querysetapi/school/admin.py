from django.contrib import admin
from .models import School ,Teacher 

# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display =['id' , 'name' , 'roll' ,'city' ,'marks' , 'pass_date']
    list_display_links = ['name']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display =['id' , 'name' , 'empnum' ,'city' , 'salary' , 'join_date']

    
