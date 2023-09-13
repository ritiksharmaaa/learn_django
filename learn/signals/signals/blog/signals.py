from django.contrib.auth.signals import user_logged_in , user_logged_out , user_login_failed
from django.contrib.auth.models import User 
from django.dispatch import receiver 
from django.core.signals import request_started , request_finished , got_request_exception 
from django.db.models.signals import pre_init , pre_save , pre_delete , post_init , post_save , post_delete 


@receiver(user_logged_in , sender=User , )
def login_success(sender , request , user ,  **kwargs):
    print("logged in signals .....")
    print("sender ", sender )
    print("request ", request )
    print("user ", user  )
    print(f'kwargs: {kwargs}' )



# user_logged_in.connect(login_success , sender=User) we can do this things via decorators . 

@receiver(user_logged_out , sender=User , )
def login_success(sender , request , user ,  **kwargs):
    print("logged out  signals .....")
    print("sender ", sender )
    print("request ", request )
    print("user ", user  )
    print(f'kwargs: {kwargs}' )



@receiver(user_login_failed  )
def login_success(sender , credentials ,  request ,  **kwargs):
    print("logged in failled  signals .....")
    print("sender ", sender )
    print("request ", request )
    # print("user ", user  )
    print(f'kwargs: {kwargs}' )


# Model signals  

def at_pre_save_receiver(sender, instance, *args, **kwargs):
    print("pre save signal called................................................ ! ")
    print('sender' , sender )
    print('instance ' ,instance  )
    print(f"kwargs: {kwargs}")



pre_save.connect(at_pre_save_receiver, sender=User)


# post_save  


def at_post_save_receiver(sender, instance, created, **kwargs):
    if created :
         print("post  save signal called ..........................................! ")
         print("new recorded............................ ")
         print("created " , created )
         print('sender' , sender )
         print('instance ' ,instance  )
         print(f"kwargs: {kwargs}")
    else:
         print("post  save signal called !..................................... ")
         print("update................. ")
         print('sender' , sender )
         print('instance ' ,instance  )
         print(f"kwargs: {kwargs}")


   



post_save.connect(at_post_save_receiver, sender=User)



# post_delete == 
#  you can set confirmation ya finally confirmation are you sure you wanr to delete this data iy user say yes it delete else noo . 


def at_pre_delete_receiver(sender, instance,  **kwargs):
    print("pre delete e signal called................................................ ! ")
    print('sender' , sender )
    print('instance ' ,instance  )
    print(f"kwargs: {kwargs}")



pre_delete.connect(at_pre_delete_receiver, sender=User)


# post_save  


def at_post_delete_receiver(sender, instance,  **kwargs):
    print("post  delete  signal called ..........................................! ")
         
    print('sender' , sender )
    print('instance ' ,instance  )
    print(f"kwargs: {kwargs}")




post_delete.connect(at_post_delete_receiver, sender=User)

# pre init and post init . 
@receiver(pre_init , sender=User)
def at_begining_init(sender , *args , **kwargs):
    print(".........................................................")
    print("pre init ..................")
    print("sender" , sender )
    print("args" , args)
    print("kwargs" ,kwargs)

    
@receiver(post_init , sender=User)
def at_ending_init(sender , *args , **kwargs):
    print(".........................................................")
    print("post init ..................")
    print("sender" , sender )
    print("args" , args)
    print("kwargs" ,kwargs)



# signals efor request and response : - 

@receiver(request_started)
def at_begining_request(sender , environ , **kwargs ):
    print("---------------------------------------------- ")
    print(" at Begining request ")
    print("sender" , sender )
    print("Environ" , environ )
    print(F"kwargs : {kwargs}")


@receiver(request_finished)
def at_begining_request(sender , **kwargs ):
    print("---------------------------------------------- ")
    print(" at end request ")
    print("sender" , sender )
    print(f"kwargs : {kwargs}")


@receiver(got_request_exception)
def at_begining_request(sender , request , **kwargs ):
    print("---------------------------------------------- ")
    print(" at request Exception  ")
    print("sender" , sender )
    print("request" , request )
    print(F"kwargs : {kwargs}")

   



