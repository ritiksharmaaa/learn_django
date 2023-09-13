from django import forms 
from .models import student , modelinheritance

class studentForm(forms.ModelForm):
    name = forms.CharField( max_length=10, required=False) # this field can overide the original fields 
    
    class Meta:
        model = student
        # fields = ['name' , 'email' , 'password']
        # exclude = ['name']
        fields = '__all__' # this will give you all field which have in 
        labels = {'name':'enter name  ' , 'email':'enter email  ' , 'password':'enter password  '}
        help_texts = {'name':'plese give name !'}
        error_messages = {'name': {'required':'nama to dena padega !'},
        'password' : {'required': "ye email dena "}}
        widgets = {'password':forms.PasswordInput,'name':forms.TextInput(attrs={'class' : 'myclass' , 'placeholder':"yahi naam likhna hai ! "}),}


# model inhertance learning 
# we have teacher_name , student_name , email , password in model 

class stuform(forms.ModelForm):
    class Meta:
        model = modelinheritance 
        fields = [ 'id' , 'student_name' , 'email' , 'password']

class teacherform(stuform):
    class Meta(stuform.Meta):
        fields = [ 'id' , 'teacher_name' , 'email' , 'password']