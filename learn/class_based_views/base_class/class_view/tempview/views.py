from django.shortcuts import render
from django.views.generic.base import TemplateView

# without making view uou just direct pass template in urls . where we can import it and call in urls . when you dont make views function . 

# # # Create your views here.
# class HomeTemplateView(TemplateView):
#     template_name = 'tempview/templateview.html' # you can pass either in url or there . 
# this is comman template methods 


# # Create your views here.and using context 
class HomeTemplateView(TemplateView):
    template_name = 'tempview/templateview.html'
 # you can pass either in url or there .

    def get_context_data(self, **kwargs):  # this kwargs have that dyanmaic url data came inside it 
        context = super().get_context_data(**kwargs)
        # we call pass this context in dict form 
        # this is affect extra_context if this has extracontext not work 
        context={
            'name' : 'ritik sharma',
            'roll' : 234
        }

        # context['name'] = " ritik sahrma" 
        # context['roll'] = 101 
        return context
     

