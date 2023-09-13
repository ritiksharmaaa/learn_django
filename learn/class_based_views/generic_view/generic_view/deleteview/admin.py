from django.contrib import admin
from .models import student 


@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' ,'email' , 'password']
    

# Register your models here.
