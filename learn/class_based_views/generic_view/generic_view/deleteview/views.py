
# Create your views here.
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .models import student
from django import forms 

# Create your views here.

#made to check how update view work 

class del_update_create_form(CreateView):
    model  = student 
    fields = ['name' , 'email' , 'password']
    template_name = 'deleteview/create.html'
    success_url = '/thankyou/'  # you create own template view to show succes 

class del_studentupdate(UpdateView):
    model = student 
    fields = ['name' , 'email' , 'password'] # field whic you want to update 
    template_name = 'deleteview/update.html' # this is option in tutorial but we do it . 
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

class studentdelview(DeleteView):
    model = student 
    success_url = '/thankyou/'
    # you can also give custom temlate name . 