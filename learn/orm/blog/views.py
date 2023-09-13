from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.


def home_page(request):
    return render(request , "blog/blog.html")

    # return HttpResponse(" i am working ")

