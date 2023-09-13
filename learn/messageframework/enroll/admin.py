from django.contrib import admin
from .models import reg_user 

# Register your models here.

@admin.register(reg_user)
class user_registerAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password']

    
