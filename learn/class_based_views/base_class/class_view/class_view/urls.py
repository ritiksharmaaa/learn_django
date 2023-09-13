"""
URL configuration for class_view project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views 
from tempview import views as tempview
from rdirect import views as rdirect 
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.my_view.as_view()), comment to check under code how to pass parameter .
    path('startschool',views.my_view.as_view(name='rahul')),
    path('childschool/',views.myviewchild.as_view(name='rahul')),
    path('aboutschool/',views.aboutnow.as_view()),
    # all views related to template view 
    # path('',tempview.TemplateView.as_view(template_name="tempview/templateview.html")),
    # path('',tempview.HomeTemplateView.as_view() , name="hometviews"), # check how to pass context 
    # path('',tempview.HomeTemplateView.as_view(extra_context={'course' : 'pytohn'})  , name="hometviews"), 
    # check  how to pass extra context  but if you pass your contect data in view so it doe't work 
    # ---------------------redirect view url s--------- 
    path('',rdirect.TemplateView.as_view(template_name="redirect.html") , name="direct run templateview "),
    # now we want to redirect to home page when we clik on next url we dont want to make a view function thant redireicet we direct use redirect view to reditrect it  
    path('redirect/',rdirect.RedirectView.as_view(url="/"), name="direct redirect eithout manual made views "), # this can redirect it directly beacue we srfe mot inherit thisclaas to our new view function .


    # redirect to extrnal links 

    path('google/' , rdirect.RedirectView.as_view(url="https://www.geekyshpws.com")),
    #with chil class redireiceView 
    path('google1/' , rdirect.Geekshow.as_view()),

    # pattern_name mean redirect with another url redirect methods 
    path('google3/' , rdirect.Geekshow.as_view(pattern_name="google")), # here when we call this url this url redirect to you by usiing go to upper url than redirect to home page or any other 
    # Also ypu can wirte pattern name inside subclass redirect method .

    path('key/<int:id>/' , rdirect.GeekRedirectView.as_view()), #we can pass pattern_name  or url value in subclass
    # but if you wan to pass dy data to reirect page you hace to use patter_name 
    # getting redirect data in tempaltes using pattern_name 
    path('<int:id>/' , rdirect.TemplateView.as_view(template_name="redirect.html")), #we can pass pattern_name  or url value in subclass


]
