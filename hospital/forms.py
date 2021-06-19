from django import forms
from django.contrib.auth.models import User
from . import models


# для формы, связанной с врачем
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'password'
                  ]
        widgets = {
            'password': forms.PasswordInput()
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ['address',
                  'mobile',
                  'department',

                  'profile_pic'
                  ]


# для формы, связанной с пациентом
class PatientUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password'
        ]
        widgets = {
            'password': forms.PasswordInput()
        }


class PatientForm(forms.ModelForm):
    assignedDoctorId = forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),
                                              empty_label="Название и отдел", to_field_name="user_id")

    class Meta:
        model = models.Patient
        fields = ['address',
                  'mobile',

                  'profile_pic'
                  ]

#
# class AppointmentForm(forms.ModelForm):
#     doctorId = forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),
#                                       empty_label="Имя врача и отделение", to_field_name="user_id")
#     patientId = forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),
#                                        empty_label="Имя пациента и симптомы", to_field_name="user_id")
#
#     class Meta:
#         model = models.Appointment
#         fields = ['description', 'status']
#
#
# class PatientAppointmentForm(forms.ModelForm):
#     doctorId = forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),
#                                       empty_label="Имя врача и отделение", to_field_name="user_id")
#
#     class Meta:
#         model = models.Appointment
#         fields = ['description', 'status']
# #
#
# # для страницы "Свяжитесь с нами"
# class ContactusForm(forms.Form):
#     Name = forms.CharField(max_length=30)
#
#     Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
