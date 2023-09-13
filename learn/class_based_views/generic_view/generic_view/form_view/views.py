from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ContactForm , FeedbackForm
from django.views.generic.base import TemplateView



# Create your views here.


class contactForm(FormView):
    template_name = 'form_view/contact.html'
    form_class =  FeedbackForm #ContactForm # here yiu have to give form name 
    success_url = '/thankyou/'
    initial = {'name':'ritik', 'email':'vim45' , 'msg':'python'}#it take dict if you want to pass some data in form input . 

    # capture data 
    def form_valid(self , form): # this method return data into success url 
        print(form)
        print(form.cleaned_data['name'])
        return super().form_valid(form)

class thankyouView(TemplateView):
    template_name = "form_view/thankyou.html"
