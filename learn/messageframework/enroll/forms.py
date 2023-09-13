from django import forms 
from .models import reg_user

class reg_form(forms.ModelForm):
    class Meta:
        model = reg_user
        fields = ['name' ,'email' , 'password']