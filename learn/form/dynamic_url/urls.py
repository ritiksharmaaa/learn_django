from django.urls import path
from . import views 

urlpatterns = [
    path("url/", views.dpage, name="dynamic_url"),
    path("bolg/<str:name>/", views.blog,   name="blog")
    
]
