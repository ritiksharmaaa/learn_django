# hook middleware in class based. 


# simple this three is normal lang  

# ek rokne ke liye view , dusra galti chupne ke liya , tisra context data changing ke liye . 

from django.shortcuts import HttpResponse
class MyprocessMiddleware:
    def __init__(self , get_response):
        self.get_response = get_response 

    def __call__(self , request):
        response = self.get_response(request)
        return response 

    # # this concept we can learn  make difrrence difrrent middleware to handle this things . use three method not use  every method in single middleware . 
    # def process_view(request , *args , **kwargs ):
    #     print(" this is process vie before views ")
    #     return HttpResponse(" this is before view ") # this is run just before view can run id set none it can run views fuction 

    # it process_view use to block views just becauseof you site is under construction show . 






    #-----------------------------------------------






        # this can run for exception came . 
    # def process_exception(self ,request , exception):
    #     print("exception occur " ) # eather print in terminal or show in web pages .
    #     # if you wnt to knoe class name so you can use magic python __class__.__name__
    #     class_name = exception.__class__.__name__
    #     print(class_name)
    #     msg = exception
    #     return HttpResponse(msg)


    def process_template_response(self , request , response  ):
        # this is not work raise nonetype object not support item assigment . 
        print("process template responds from middleware")
        response.context_data['name'] = 'Sonam'
        return response