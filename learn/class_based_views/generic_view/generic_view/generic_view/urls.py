"""
URL configuration for generic_view project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Views_generic import views 
from detail_view.views import StudentDetailView ,  stuDetailView
from form_view.views import contactForm , thankyouView

from createview.views import Student_create_view
from updateview.views import update_create_form , studentupdate
from deleteview.views import del_update_create_form , del_studentupdate , studentdelview
urlpatterns = [
    path('admin/', admin.site.urls),

    # list views -----------------------------------
    path('default/', views.StudentListView.as_view() , name="student_list_view"),
    path('custom/', views.studentlistview.as_view() , name="student_custom_listview"),
    path('mcustom/', views.stulistview.as_view() , name="more_student_custom_list_view"),


    #detailviews -------------------------
    path('<int:pk>/', StudentDetailView.as_view() , name="detailview_cutom") ,# callwith pk or slug 
    path('custom/<int:pk>/', stuDetailView.as_view() , name="detailview_cutom"), #  #custom detai; view with cutom tem and context 
    path("formview/", contactForm.as_view(), name="fromView"),
    path("thankyou/", thankyouView.as_view(), name="fromViewthankyou"),

    # create views 

    path('create/',Student_create_view.as_view(), name='createview start '),


    # update view 
    path('upcreate/', update_create_form.as_view(), name='update - createview to check updateview '),
    path('upcreate/<int:pk>/',studentupdate.as_view(), name='updating fields'),


    # delete view 

    # update view 
    path('delupcreate/', update_create_form.as_view(), name='update - createview to check updateview  in delete '),
    path('delupcreate/<int:pk>/',studentupdate.as_view(), name='updating fields in delte '),
    path('delupcreatedel/<int:pk>/',studentdelview.as_view(), name='delete objects '),
]
#  programing\django\learn\class_based_views\generic_view\generic_view