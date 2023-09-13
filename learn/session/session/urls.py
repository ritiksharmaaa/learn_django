"""
URL configuration for session project.

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
from page_session_expire import views as demo 
from file_session import views as f 
from framwork import views as fwork 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/', demo.get , name="get_session"),
    path('set/', demo.set , name="set_session"),
    path('del/', demo.dt ,name="del_session"),
    path('fget/', f.get , name="get_session"),
    path('fset/', f.set , name="set_session"),
    path('fdel/', f.dt ,name="del_session"),
    path('fworkset/', fwork.setsession , name="setsession"),
    path('fworkget/', fwork.getsession , name="getsession"),
    path('fworkdel/', fwork.delsession , name="delsession"),
]
    # path('fdel/', fworkf.dt ,name="del_session"),

