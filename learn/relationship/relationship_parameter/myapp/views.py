from django.shortcuts import render
from django.contrib.auth.models import User 
from .models import Page ,Post ,Song 

# Create your views here.

def home(request):
    return render(request , 'myapp/home.html')

def user(request):
    date1 = User.objects.all()
    date2 = User.objects.filter(email='amulya@mail.com')
    # date3 = User.objects.filter(page__page_cat="family")
    date3 = User.objects.filter(mypage__page_cat="family")# using related_name 
    date4 = User.objects.filter(post__post_publish_date='2023-8-31')
    date5 = User.objects.filter(song__song_duration=4)

    context = {
        'date1' : date1,
        'date2' : date2,
        'date3' : date3 ,
        'date4' : date4 ,
        'date5' : date5 ,
    }

    return render(request , 'myapp/user.html',  context )


def page(request):
    date1 = Page.objects.all()
    date2 = Page.objects.filter(page_cat='dance')
    date3 = Page.objects.filter(user__email='_ritiksharmaaa@gmail.com')

    
    context = {
        'date1' : date1,
        'date2' : date2,
        'date3' : date3 }
    return render(request , 'myapp/page.html' ,  context )



def post(request):

    date1 = Post.objects.all()
    date2 = Post.objects.filter(post_publish_date='2023-08-31')
    date3 = Post.objects.filter(user__username='amulya')

    context={
         'date1' : date1,
        'date2' : date2,
        'date3' : date3 

    }
    return render(request , 'myapp/post.html' ,context )


    

def song(request):
    date1 = Song.objects.all()
    date2 = Song.objects.filter(song_duration='4')
    date3 = Song.objects.filter(user__username='amulya')

    context={
         'date1' : date1,
        'date2' : date2,
        'date3' : date3 

    }
   
    return render(request , 'myapp/song.html' ,context )
    

