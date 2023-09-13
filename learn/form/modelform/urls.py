from django.urls import path
from . import views  

urlpatterns = [
    path("form/",views.mform_page , name="model form "),
    path("del/<int:id>/", views.page_delete, name="delete"),
    path("upt/<int:id>/", views.update_page, name="delete"),
    path("inherit/", views.forminherit, name="form inherit"),
]
