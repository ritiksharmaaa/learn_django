from  django.contrib.auth.models import User 
from django import forms 
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UserChangeForm


class signup(UserCreationForm):
    #password2 is inside usercreationform we can overide and change label 
    password2 = forms.CharField(label='Confirm Password (again)')
    class Meta: 
        model = User 
        #password is not in this field because it has manually writen in usercreationform 
        fields = ['username' , 'first_name' ,'last_name' , 'email']
        labels = {'email' : 'Email'}


# class signin():
#     pass 

class userProfile(UserChangeForm):
    password = None 
    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name' , 'email' ,'date_joined' ,'last_login']
        labels = {'email' : 'Email'}