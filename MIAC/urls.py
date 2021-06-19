from django.contrib import admin
from django.urls import path

from addbdinf import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/doctor_signup_view', views.doctor_signup_view, name='doctor_signup_view'),
    path('doctor_dashboard_view', views.doctor_dashboard_view, name='doctor_dashboard_view'),
    path('doctor_add_patient_view', views.doctor_add_patient_view, name='doctor_add_patient_view'),

    path('patient_signup_view', views.patient_signup_view , name='patient_signup_view'),
    path('patient_dashboard_view', views.patient_dashboard_view, name='patient_dashboard_view'),
    path('patient_sending_a_message_view', views.patient_sending_a_message_view, name='patient_sending_a_message_view'),

    # path('', views., name=''),
    # path('', views., name=''),
    # path('', views., name=''),
]
