from django.urls import path 
from .views import profileTemplateView
from django.contrib.auth.decorators import login_required 

urlpatterns = [
    path("profile/", login_required(profileTemplateView.as_view()), name="profile")
]
