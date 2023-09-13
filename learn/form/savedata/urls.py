from django.urls import path
from .  import views 

urlpatterns = [
    path("form/", views.main_page, name=""),
    path("update/<str:id>/", views.update, name="update" ),
    path("delete/<str:id>/", views.delete, name="delete")
]