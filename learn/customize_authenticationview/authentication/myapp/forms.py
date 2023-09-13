#We have to see the source code inside the inside the jungle liability called authentication forms where we can see how we have to make your own custom formso we can give into a class based views . 
from django import forms 
from django.contrib.auth.forms import AuthenticationForm , UsernameField
from django.utils.translation import gettext , gettext_lazy as _


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class' : "monkey raja" , 
    'autofocus' : True }))
    password = forms.CharField(label=_("password") ,strip=False , widget=forms.PasswordInput(attrs={'class' : 'my raja ', 'autocomplete' : 'current-password' , }) ,)


# we can pass form even inurl file 