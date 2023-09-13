from django.contrib import admin
from .models import Post , Song

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user' , 'post_title' , 'post_cat' , 'post_publish_date']
    
@admin.register(Song)
class Admin(admin.ModelAdmin):
    list_display = ['id' , 'song_name' , 'song_duration' , 'writenby']
