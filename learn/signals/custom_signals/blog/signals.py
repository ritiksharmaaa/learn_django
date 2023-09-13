# custom signals makking . 
from django.dispatch import Signal
notification = Signal()

 #reciver function : ---
 

def notification_show (sender, **kwargs):
    print(" i am custom signal printed in terminal .............................. ")
    print("sender" , sender )
    print(f"kwargs : {kwargs}" )
    print("notification")


notification.connect(notification_show)