"""
URL configuration for authentication project.

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
from account import views 
from . import views as main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.home_page , name="home"),
    path('profile/', main.profile_page , name="profile" ),
    path('dashboard/', views.dashboard , name="dashboard" ),
    path("singup/",views.sing_up, name="singup"),
    path("singin/",views.log_in, name="singin"),
    path("logout/",views.log_out, name="logout"),
    path("passchange/",views.password_change, name="passchange"),
    path("passchange2/",views.password2_change, name="passchange2")
]
