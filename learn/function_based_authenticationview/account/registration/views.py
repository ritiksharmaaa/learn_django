from django.shortcuts import render

from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
# D:\programing\django\learn\function_based_authenticationview>
@login_required  # we learn how to use perm and login required . 
def profile(request):
    return render(request , 'registration/profile.html')

@staff_member_required
def staffprofile(request):
    return render(request , 'registration/profile.html')