from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView 



class profileTemplateView(TemplateView):
    template_name = "registration/profile.html"

