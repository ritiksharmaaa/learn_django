from django import forms 
from django.core import validators


class saveform(forms.Form):
    name = forms.CharField( error_messages={'required': 'Please give your Name !  '})
    email = forms.EmailField(    error_messages={'required': 'Please give your Email  !  '} , min_length=5 , max_length=50 )
    password = forms.CharField(widget=forms.PasswordInput() , error_messages={'required': 'Please give your passwords  !  '} , min_length=5 , max_length=50)
    password2 = forms.CharField( widget=forms.PasswordInput() ,error_messages={'required': 'Please type again passwords  !  '} , min_length=5 , max_length=50)


    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('password')
        pass2 = cleaned_data.get('password2')
        if pass1 != pass2:
            raise forms.ValidationError("password does not match ")


   # this is method 2 use to sasve formapi data 
    # def update(self ,instance):
    #     for field , value in self.cleaned_data.items():
    #         setattrs(instance ,field ,value)
    #         instance.save()
