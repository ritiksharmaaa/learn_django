from django.shortcuts import render
from django.http import HttpResponse
from .forms import user



# Create your views here.

def form_api(request):
    fm =  user(auto_id='some_%s' , label_suffix=' - !' , initial = {'name' : 'ritik sharma' , 'email':'ritiksharma18@gmail.com'})
    fm.order_fields(field_order = {'email', 'name'})
    context = {
        'form' : fm

    }
    return render(request , "form/form.html" , context)
    # return HttpResponse(" this  is from main page ! ")