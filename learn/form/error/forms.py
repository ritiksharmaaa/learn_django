from django import forms 
from django.core import validators 

class styile(forms.Form):
    name = forms.CharField( error_messages={'required': 'Please give your Name !  '})
    email = forms.EmailField(    error_messages={'required': 'Please give your Email  !  '} , min_length=5 , max_length=50 )
    password = forms.CharField(widget=forms.PasswordInput() , error_messages={'required': 'Please give your passwords  !  '} , min_length=5 , max_length=50)
    password2 = forms.CharField( widget=forms.PasswordInput() ,error_messages={'required': 'Please type again passwords  !  '} , min_length=5 , max_length=50)


    def match(self):
        data = self.cleaned_data.get('password')
        data2 = self.cleaned_data.get('password2')
        if data != data2:
            raise forms.ValidationError("password does not match ")





#styiling form as it not specfic target . 


class styile2(forms.Form):
    error_css_class = 'cusclass'
    required_css_class = 'required'

    name = forms.CharField( error_messages={'required': 'Please give your Name !  '})
    email = forms.EmailField(    error_messages={'required': 'Please give your Email  !  '} , min_length=5 , max_length=50 )
    password = forms.CharField(widget=forms.PasswordInput() , error_messages={'required': 'Please give your passwords  !  '} , min_length=5 , max_length=50)
    password2 = forms.CharField( widget=forms.PasswordInput() ,error_messages={'required': 'Please type again passwords  !  '} , min_length=5 , max_length=50)



    # def error(self):
    #     print("error logiging ")
    #     data = self.cleaned_data["name"]
    #     if len(date) < 5 :
    #         raise forms.ValidationError(" plese provide more than five char ! ")
            
            




    
