from django.contrib import admin
from .models import *


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'department', 'mobile', ]


class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'age', 'gender', 'mobile', 'snils' ]


class data_PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'patientId', 'pressure', 'pulse', 'date', 'time', ]


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(data_Patient, data_PatientAdmin)
