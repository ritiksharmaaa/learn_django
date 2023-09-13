from django.shortcuts import render
from django.core.cache import cache 

# Create your views here.

# def home(request):
#     mv =  cache.get_or_set('fees' , '4000' , 30 )
#     # we ahve more simple way to do this 

#     # mv = cache.get('movie' ,'has_expired')
#     # if mv == 'has_expired' :
#     #     cache.set('movie','dilwale' , 30)
#     #     mv =  cache.get('movie')
#     return render(request , 'course.html' , {'fm' : mv })

def home(request):
    data = { 'name' : 'ritik' , 'class' : '4' ,  'roll': 401 } 
    cache.set_many(data ,30 )
    sv =  cache.get_many(data)
    print(sv)
    return render(request , 'course.html' ,{'fm' : sv})