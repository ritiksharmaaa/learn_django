from django.shortcuts import render
from django.views.generic.detail import DetailView
from Views_generic.models import student 

# Create your tests here.


class StudentDetailView(DetailView):
    model = student # data get inside template student.id 
    # template_name = "TEMPLATE_NAME" # default is end with _detail.html

# Create your views here.


class stuDetailView(DetailView):
    model = student
    template_name = "school/custom_delta.html" # you can also define template indside as_view() 
    context_object_name = "stu"
    # pk_url_kwarg = 'id' # url id define 
    
    # getting extra context to getting all name of this model in detail view 
    def get_context_data(self,*args ,  **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_student"] = self.model.objects.all()
        return context
    
