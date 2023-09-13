from django import forms 

class contactforms(forms.Form):
    name = forms.CharField( max_length=45, required=False)
    surname = forms.CharField( max_length=45, required=False)
    roll = forms.IntegerField(required=False)