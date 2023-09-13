from django.shortcuts import render

# Create your views here.
def hoem_page(request):
    return render(request , 'home.html')

def test(request , year ):
    return render(request , 'test.html' ,{'year' : year})