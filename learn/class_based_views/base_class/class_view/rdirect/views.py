from django.shortcuts import render
from django.views.generic.base import TemplateView , RedirectView 

# Create your views here.

# child redirect view 

class Geekshow(RedirectView):
    url = "https://geekyshows.com"


# geting dynamic data came with url and redirect to paticaular page 
class GeekRedirectView(RedirectView):
    # url= '/'
    pattern_name=""
    # when ever redirect happen permananet  = true give 302 code "
    permanent = True 
    # querry string  mean after dynamic data pass 12?lbancffca so tgibris code hode on url bar tabs hide if false . show if true 
    query_string=True # you can also pass data like that 12?name=riitk - so this dat ayiu can also pass 

    def get_redirect_url(self , *args , **kwargs):
        print(kwargs)
        #also modeife or reconstruct 
        kwargs[id] = 24
        return super().get_redirect_url(*args , **kwargs)
    
     
