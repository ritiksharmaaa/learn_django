from django import forms 

class argsform(forms.Form):
    name = forms.CharField( required=True , label="Your Name " , label_suffix=": - " , initial="Ritik Sharma"  , help_text="please give valid")
    email = forms.EmailField( required=False ,  label="Your Email " , label_suffix=" : -" , initial="Ritksharma12@gmail.com" , disabled=True )
    surname = forms.CharField(widget=forms.TextInput(attrs={'class' : 'surname surmale',
    'id' : 'sur_id'}))
    
