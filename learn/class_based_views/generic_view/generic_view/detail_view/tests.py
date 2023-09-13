from django.test import TestCase
from django.views.generic.detail import DetailView

# Create your tests here.


class StudentDetailView(DetailView):
    model = Student
    template_name = "TEMPLATE_NAME" # default is end with _detail.html
    

