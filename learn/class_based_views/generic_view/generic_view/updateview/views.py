from django.shortcuts import render
from django.views.generic.edit import CreateView , UpdateView
from .models import student
from django import forms 

# Create your views here.

#made to check how update view work 

class update_create_form(CreateView):
    model  = student 
    fields = ['name' , 'email' , 'password']
    template_name = 'updateview/create.html'
    success_url = '/thankyou/'  # you create own template view to show succes 

class studentupdate(UpdateView):
    model = student 
    fields = ['name' , 'email' , 'password'] # field whic you want to update 
    template_name = 'updateview/update.html' # this is option in tutorial but we do it . 
    success_url = '/thankyou/'  # you create own template view to show succes . or give get abslote url 

    # how we put clasess we can use either get_form method or give model form . 

    # via get_form

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget= forms.TextInput(attrs={
            'class' : "lichi rani nani",
        })
        form.fields['email'].widget= forms.TextInput(attrs={
            'class' : "lichi rani nani",
        })
        form.fields['password'].widget= forms.PasswordInput(attrs={
            'class' : "lichi rani nani",
        })
        return form 


        # another methods just five models form 
        # form_class = model form  in crete view - so you have to use this methods alse upper methods . 
        # whatever you define class in model for autmatical came there . 



