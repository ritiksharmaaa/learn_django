from django.contrib import admin
from .models import createview_student

# Register your models here.

@admin.register(createview_student)
class createview_studentAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'email' , 'password')
    

