from django import forms

class fpost(forms.Form):
    name = forms.CharField( max_length='400', required=False)
    email = forms.EmailField( required=False)
    password = forms.CharField(widget=forms.PasswordInput() , max_length= 400 , required=False)

