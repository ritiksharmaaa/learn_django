from django.shortcuts import render
from .models import Post 
from django.views.generic import ListView , DetailView
from django.http import Http404
from django.core.paginator import Paginator

# Create your views here.

def blog_post(request):
    blog = Post.objects.all().order_by('-id')
    paginator = Paginator(blog , 3 )
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) # this tell how many page you have and data 
    print(page_obj)
    return render(request , 'blog/blog.html' , {'page_obj' : page_obj})



# ----------------------class based pagination ---------------
class blog_post_class(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering= ['-id']
    paginate_by = 3
    paginate_orphans = 1 # mean if last page have only one it can shiffted 3 to four .
    # page_obj we alredy see this attribute in listview . 
    # here if you give unwated page no or string in page = so it gave error . - in function it alredy manage. it 
    # only last instace maintain .

    # # handeling last paramete in post=  
    # def get_context_data(self, **kwargs):
    #     try:
    #         return super(blog_post_class , self).get_context_data(**kwargs)
    #     except Http404:
    #         self.kwargs['page'] = 1
    #         return super(blog_post_class, self).get_context_data(**kwargs)
            

    #----------more methods 

    def paginate_queryset(self , queryset , page_size):
        try:
            return super(blog_post_class , self).paginate_queryset( queryset , page_size)
        except Http404:
            self.kwargs['page'] = 1
            return super(blog_post_class, self).paginate_queryset(queryset , page_size)

    # we have a is_paginate to verify it 


class postDetailView(DetailView):
    model = Post 
    print(model)
    template_name = 'blog/detail.html'
            

             
    