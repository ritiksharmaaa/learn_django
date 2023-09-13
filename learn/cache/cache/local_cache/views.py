from django.shortcuts import render

# Create your views here.
def home(request):
    print("iam runnnig ")
    return render(request , 'course.html')
