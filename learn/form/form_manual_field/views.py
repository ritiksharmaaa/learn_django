from django.shortcuts import render
from django.http import HttpResponse
from .forms import mForm 
# Create your views here.
def mform(request):
    fm = mForm()
    context = {
        'form' : fm
    }
    return render(request , 'mform.html' , context)
    # return HttpResponse(" i am mform with mannual from render !")
    
