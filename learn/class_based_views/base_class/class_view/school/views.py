from django.shortcuts import render , HttpResponse 
from django.views import View # we can aslo get this view from genric 
from .forms import contactforms

# Create your views here.

# function basde view we have know 

#classed based view
class my_view(View): # if want to pass paramet pass inside as_view() method on urls 
    name = 'sonam' # this can be overighted when we pas data from as_view() 

    def get(self ,request):
        return render(request , 'home.html')
        # return HttpResponse( self.name) comment to render html page 

# we can use upper code in child class ;

class myviewchild(my_view):
    def get(self , request):
        return HttpResponse(self.name) # this name can be pass from upper ingertance code .

 # check how can pass context data 


class aboutnow(View):
    context = {
        'msg' : 'welcome to geekshows function based views '
    } # if you write there you need to use it by self.methods . it not want define inside class methods 
    def get(self , request):
        form = contactforms()
        return render (request , 'about.html' , {'form' : form})
        #  return render(request , 'about.html' , self.context ) comment to check upper code render form
    def post(self , request):
        fm = contactforms(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data.get('name')
            print(name)
            return HttpResponse("form get susssefully ")

##############################form pass inside class -------- to learn post method also -


# If you want to make another function and you want it to render two template in different different time so via dynamically passing the template in our urls and it can work same

#Example we have a url called About and in the view after the view we inside and sat V in a lies a key and a word and these keywords are using in views functionand we will store these names as a template and render at the render time we are using the render template variable the variable which the variable they are came from the url.

#Again we can make a contact 1URLand we also passing same view function but in url we are passing different template name directory and in same view function we getting these template name and store in a variable and renderthe template by dynamically which are we getting from the url so its help us to use different template in a single view functionbut multiple url. 

# path('contact/' , views.contact , {'template_name : 'school/contact1.html' })
# path('contac2t/' , views.contact , {'template_name : 'school/contact2.html' })
# both have same function called contact 

#in functioj dtore this dir in variable and 

# rettun render(request , template_dir_var , context )


