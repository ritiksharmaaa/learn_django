def my_middleware(get_response):
    print(" one time initialization ! ")
    def my_function(request):
        print(" run before views reponse")
        response = get_response(request)
        print("this is running after views ")
        return response
    return my_function



# ------------------------------ class based middleware ----------------- 


class mymiddleware:
    def __init__(self , get_response):
        self.get_response= get_response
        print(" one time initialization in class based middleware ")
        # one time initialization 
    def __call__(self , request):
        print(" running class middleware before in class based  ")
        #code to be excuted for each request before the views (and later middleware) are called 
        response = self.get_response(request) # write http response if not tranfer to another middleware . 
        print(" running class middleware after in class based ")
        # code to be excuted for each request/response after the views is called .
        return response 