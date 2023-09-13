from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import createview_student

from django import forms
# D:\programing\django\learn\class_based_views\generic_view\generic_view>
# Create your views here.

# it create form and save data to model by generic create view 

class Student_create_view(CreateView):
    model = createview_student
    fields = ['name' , 'email' ,'password']
    template_name = 'createview/createview_student.html'
    # success_url = '/thankyou/'  # this url is not for this app so we give another app sucess url ----------commemy to check model function 
    # but we can define url by success_url 
    # here if you submitt data it say define url or provide get_abslote_url in model  -- but data is submiteed alredy 

    #add classes in form  by first way 

    def get_form(self):
       form =  super().get_form()
       form.fields['name'].widget = forms.TextInput(attrs={ # here forms are not define so we have to import it 
        'class' : " mango banana shake" ,
        'placeholder' : "tera naam",
       })
       form.fields['email'].widget = forms.TextInput(attrs={ # here forms are not define so we have to import it 
        'class' : " mango banana shake" ,
        'placeholder' : "tera email",
       })
       form.fields['password'].widget = forms.PasswordInput(attrs={ # here forms are not define so we have to import it 
        'class' : " mango banana shake" ,
        'placeholder' : "tera password ",
       })
       return form 


       # by second way 
    #    you have model  now create model form with that model 

    ''' in model form you can do what class you nedd we learn in model form 
    or just do inside class where we write model = model , 
    now we have to write form_class = modelform that is and give template 

    second was a good methods . '''









"""  how to define clasess in form . 

we have two way to add class 

overite get_form """