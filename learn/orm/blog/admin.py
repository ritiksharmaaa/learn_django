from django.contrib import admin
from . models import (blog ,  post , authore , book , Vehicle , Car ) 
# Register your models here.


# admin.site.register(blog)

@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    list_display=( "id", "blog_title" , "blog_desc" , "blog_like" , "create_by")

# @admin.register(user)
# class userAdmin(admin.ModelAdmin):
#     list_display=("id", "user_name" , "user_pass")

@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display=( "id" , "post_title" , "post_cat" , "user")



@admin.register(authore)
class authoreAdmin(admin.ModelAdmin):
    list_display = ( "authore_name" ,   "id" , "authore_desc")
    

@admin.register(book)
class bookAdmin(admin.ModelAdmin):
    list_display = ( "btitle"  , "bdesc" , "writen_by")

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("reg_no" , "owner")
    list_display_links = ("reg_no" , "owner")

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("car_model" , "own_by")
    

    

    
    



    

    
