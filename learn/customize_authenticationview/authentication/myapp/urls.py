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

from django.urls import path
from django.contrib.auth import views as auth_view
from myapp.forms import LoginForm
urlpatterns = [
    path('login/' , auth_view.LoginView.as_view(template_name='myapp/login.html' , authentication_form=LoginForm) , name='login'),
    path('logout/' , auth_view.LogoutView.as_view(template_name='myapp/logout.html') , name='logout')
]
# same as you can use it for each urls . 