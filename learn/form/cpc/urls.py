from django.urls import path , register_converter

from . import views , converter

register_converter(converter.FourDigitYearConverter , 'yyyy') # tell write where str:no now we use yyyy:year



urlpatterns = [
    path("url/", views.hoem_page ,  name="home-page"),
    path("<yyyy:year>/", views.test ,  name="home-page"),
    
]
