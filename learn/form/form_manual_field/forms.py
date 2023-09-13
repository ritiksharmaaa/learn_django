from django import forms 

class mForm(forms.Form):
    name = forms.CharField(initial="ritik_sharma " , help_text="please give at least 30 words ")
    surname = forms.CharField()
    email = forms.EmailField()
    

