from django.urls import path, include

from . import views

urlpatterns = [
    path('api/View_Doctor_signup', views.View_Doctor_signup.as_view(), name='get-View_Doctor_signup'),
    path('api/View_Patient_signup', views.View_Patient_signup, name='get-View_Patient_signup'),
    path('api/View_data_Patient', views.View_data_Patient.as_view(), name='get-View_data_Patient'),

]
