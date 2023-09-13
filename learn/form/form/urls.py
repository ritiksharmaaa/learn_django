"""
URL configuration for form project.

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
from django.urls import path , include 
from formapi import views
from form_manual_field import views as t
from form_field_argument import views as a 
from formpost import views as f
from fft import views as ft 
from error import views as error 


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.form_api),
    path("mform/" , t.mform , name="mform"),
    path("fargs/", a.f_args , name="fargs"),
    path("fpost/", f.formpost , name="fpost"),
    path("thankyou/" ,f.thankyou , name = "thankyou"),
    path("fft/", ft.fft , name=" form field type "),
    path("cfv/", ft.cfv , name="custom form validator "),
    path("error/",error.error_page, name="error pages "),
    path("error2/",error.error_page2, name="error pages "),
    path("save/", include("savedata.urls")),
    path("model/", include('modelform.urls')),
    path("dynamic/", include('dynamic_url.urls')),
    path("converter/", include('cpc.urls')),
    
]
