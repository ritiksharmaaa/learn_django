from django.shortcuts import render
from .models import student 
from django.views.generic.list import ListView
# Create your views here.

class StudentListView(ListView):
    model = student   # this data passe in template with object_list  - ex model_list = where model is model name 
    # if default you have to make a template who labelsuffix _list.html is impo 

# custom list view 

class studentlistview(ListView):
    model = student
    template_name_suffix = '_get' # mean html end with _get than it rendered 
    ordering = ['course'] # order data via name 


# more custom ------------------------------list view 

class stulistview(ListView):
    model = student
    template_name = 'Views_generic/more_custom_student.html'
    context_object_name = 'students' # custom objects name 

    # in model manage we use in function to get custom data here we make function to get this 

    def get_queryset(self):
        return student.objects.filter(course="docker")

    # we are getting custom data with loower function . we dont need to get data from students 

    # here we see we can get multiple objects , rather than defsult / we can use for passing form aslo 
    def get_context_data(self , *args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['fresher'] = student.objects.all().order_by('name')
        return context 
        # this call in template like this for stu in fresher 
    # ---------------------------
    # in function we have option to display templated dynamically by passing in tempalte name in url or also check bu own function so change this template to this template . 
    
    def get_template_names(self):
        print(' i am running ')
        # giving condition 
        if self.request.user.is_superuser:
            print(" inside cookie")
            self.template_name = 'Views_generic/dynamic_template_render.html'
        else:
            print('outside cookie')
            template_name = self.template_name
        return [template_name]

    # def get_template_names(self):
    #     print(' i am running ')
    #     # giving condition 
    #     if self.request.COOKIES['user'] == 'ritik':
    #         print(" inside cookie")
    #         self.template_name = 'Views_generic/dynamic_template_render.html'
    #     else:
    #         print('outside cookie')
    #         template_name = self.template_name
    #     return [template_name]