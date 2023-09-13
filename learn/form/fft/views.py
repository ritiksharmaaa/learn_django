from django.shortcuts import render
from .forms import fftForm , custom_validation
# from django.http import HttpResponse 



# Create your views here.
def fft(request):
    if request.method == 'POST':
        fm = custom_validation(request.POST)
        if fm.is_valid():
            print('Form Validation ! ')
            print(request.POST.get('email'))
            print(request.POST.get('surname'))
            print(request.POST.get('roll'))
            print(request.POST.get('price'))
            print(request.POST.get('name'))
            print(request.POST.get('rates'))
            print(request.POST.get('accept'))
    else : 
        fm = custom_validation()

    return render(request , 'fft.html' , {'form' : fm })


def cfv(request):
    if request.method == 'POST' :
        form = custom_validation(request.POST)
        if form.is_valid():
            print("form validated")
            print(request.POST.get('name'))
    else :
        form = custom_validation()
        
    return render (request ,'cfv.html' , { 'form' : form  })


