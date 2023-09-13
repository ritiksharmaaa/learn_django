from django import forms
from django.core import validators 


class fftForm(forms.Form):
    name = forms.CharField( required=True  , min_length=5 , max_length=15  , strip=False , empty_value="ritkwerwe")
    surname  = forms.CharField( error_messages={'required' : ' please enter a surname'} ,)
    email = forms.EmailField( required=False)
    roll = forms.IntegerField(min_value=5 ,max_value=10)
    price = forms.DecimalField(min_value=10 ,max_value=1000 , max_digits=4 , decimal_places=1)
    rates = forms.FloatField(min_value=5,max_value=10)
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 3 , 'cols' : 50}))
    accept  = forms.BooleanField( label="agree" ,)






class custom_validation(forms.Form):
    name = forms.CharField( error_messages={'required': 'please give rigth Information '})
    surname = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()
    time = forms.CharField(validators=[validators.MaxLengthValidator(10)])


    def clean(self):
        cleaned_data = super().clean()
        name = self.cleaned_data.get('name')
        if name == "radha":
            raise forms.ValidationError(" radha is suspended for 5 day ")
        sname = self.cleaned_data.get('surname')
        if sname == "mishra":
            raise forms.ValidationError("all mishara suspended ")

        pas1  = self.cleaned_data.get('password')
        if pas1 == '123456' :
            raise forms.ValidationError("abe lamba password de ")

        pas2  = self.cleaned_data.get('password2')
        if pas2 != pas1:
            raise forms.ValidationError("password does not match   ")


# this is used when we validate one  field see uper code to whole valisation 
    # def clean_name(self):
    #     nm = self.cleaned_data.get('name')
    #     if len(nm)< 4 :
    #         raise forms.ValidationError('abe sahi name daal na ')



    

    
