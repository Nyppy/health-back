from django.views import View
from django.http import JsonResponse

from . import forms, models
from .models import Categories, CouponsOjects
import json
import base64
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *

from django.views.decorators.csrf import csrf_exempt

def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()


def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()


class View_Doctor_signup(View):
    def get(self, request):
        data = Doctor.objects.all()

        list_data = {'data': []}
        for j in data:
            list_data['data'].append(
                {
                    'first_name': j.first_name,
                    'last_name': j.last_name,
                    'profile_pic': j.profile_pic,
                    'address': j.address,
                    'mobile': j.mobile,
                    'departament': j.department

                })
            return JsonResponse(list_data)

    def post(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)

            doctor = Doctor.objects.create(
                last_name=data.last_name,
                first_name=data.first_name,
                profile_pic=data.profile_pic,
                address=data.address,
                mobile=data.mobile,
                department=data.departament
            )
            doctor.save()

            return JsonResponse({
                'first_name': doctor.first_name,
                'last_name': doctor.last_name,
                'profile_pic': doctor.profile_pic,
                'address': doctor.address,
                'mobile': doctor.mobile,
                'departament': doctor.departament,
            })


@csrf_exempt
class View_Patient_signup(View):
    def get(self, request):
        data = Patient.objects.all()

        list_data = {'data': []}
        for i in data:
            list_data['data'].append(
                {
                    'first_name': i.first_name,
                    'last_name': i.last_name,
                    'gender': i.gender,
                    'age': i.age,
                    'profile_pic': i.profile_pic,
                    'address': i.address,
                    'mobile': i.mobile,
                    'snils': i.snils,
                    'assignedDoctorId': i.assignedDoctorId,
                    'id': i.pk,

                })
            return JsonResponse(list_data)
    
    def post(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)

            patient = Patient.objects.create(
                last_name=data.last_name,
                first_name=data.first_name,
                gender=data.gender,
                age=data.age,
                profile_pic=data.profile_pic,
                address=data.address,
                mobile=data.mobile,
                snils=data.snils,
                assignedDoctorId=data.assignedDoctorId
            )
            patient.save()

            return JsonResponse({
                'first_name': patient.first_name,
                'last_name': patient.last_name,
                'gender': patient.gender,
                'age': patient.age,
                'profile_pic': patient.profile_pic,
                'address': patient.address,
                'mobile': patient.mobile,
                'snils': patient.snils,
                'assignedDoctorId': patient.assignedDoctorId,
            })


class View_data_Patient(View):
    def get(self, request):
        data = data_Patient.objects.all()

        list_data = {'data': []}
        for i in data:
            list_data['data'].append(
                {
                    'patientId': i.patientId,
                    'pressure_U ': i.pressure_U,
                    'pressure_D ': i.pressure_D,
                    'pulse ': i.pulse,
                    'date ': i.date,
                    'time ': i.time,
                    'complaints ': i.complaints,
                })
            return JsonResponse(list_data)

    def post(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)

            data_patient = data_Patient.objects.create(
                patientId=data.patientId,
                pressure_U=data.pressure_U,
                pressure_D=data.pressure_D,
                pulse=data.pulse,
                date=data.date,
                time=data.time,
                complaints=data.mobile,
            )
            data_patient.save()

            return JsonResponse({
                'patientId': data_patient.patientId,
                'pressure_U ': data_patient.pressure_U,
                'pressure_D ': data_patient.pressure_D,
                'pulse ': data_patient.pulse,
                'date ': data_patient.date,
                'time ': data_patient.time,
                'complaints ': data_patient.complaints,
            })

#
# @user_passes_test(is_doctor)
# def doctor_dashboard_view(request):
#     patientcount = models.Patient.objects.all().filter(status=True, assignedDoctorId=request.user.id).count()
#     mydict = {
#         'patientcount': patientcount,
#         'doctor': models.Doctor.objects.get(user_id=request.user.id),
#     }
#     return render(request, 'hospital/doctor_dashboard.html', context=mydict)

#
# @user_passes_test(is_doctor)
# def doctor_add_patient_view(request):
#     userForm = forms.PatientUserForm()
#     patientForm = forms.PatientForm()
#     mydict = {'userForm': userForm, 'patientForm': patientForm}
#     if request.method == 'POST':
#         userForm = forms.PatientUserForm(request.POST)
#         patientForm = forms.PatientForm(request.POST, request.FILES)
#         if userForm.is_valid() and patientForm.is_valid():
#             user = userForm.save()
#             user.set_password(user.password)
#             user.save()
#
#             patient = patientForm.save(commit=False)
#             patient.user = user
#             patient.status = True
#             patient.assignedDoctorId = request.POST.get('assignedDoctorId')
#             patient.save()
#
#             my_patient_group = Group.objects.get_or_create(name='PATIENT')
#             my_patient_group[0].user_set.add(user)
#
#         return HttpResponseRedirect('doctor-view-patient')
#     return render(request, 'hospital/doctor_add_patient.html', context=mydict)

#
# class patient_dashbord_View(View):
#     def get(self, request):
#         data1 = Patient.objects.all()
#         data2 = Doctor.objects.all()
#
#         list_data1 = {'data1': []}
#         list_data2 = {'data2': []}
#         for i in data1:
#             list_data1['data1'].append(
#                 {
#                     'first_name': i.first_name,
#                     'last_name': i.last_name,
#                     'gender': i.gender,
#                     'age': i.age,
#                     'profile_pic': i.profile_pic,
#                     'address': i.address,
#                     'mobile': i.mobile,
#                     'snils': i.snils,
#                     'assignedDoctorId': i.assignedDoctorId,
#
#                 })
#             for j in data2:
#                 list_data2['data2'].append(
#                     {
#                         'first_name': j.first_name,
#                         'last_name': j.last_name,
#                         'profile_pic': j.profile_pic,
#                         'address': j.address,
#                         'mobile': j.mobile,
#                         'departament': j.department
#
#                     })
#             return JsonResponse(list_data1, list_data2)
#
#     def post(self, request):
#         if request.method == 'POST':
#             data = json.loads(request.body)
#
#             patient = Patient.objects.create(
#
#             )

#
# @user_passes_test(is_patient)
# def patient_dashboard_view(request):
#     patient = models.Patient.objects.get(user_id=request.user.id)
#     doctor = models.Doctor.objects.get(user_id=patient.assignedDoctorId)
#     data_Patient = models.data_Patient.objects.all()
#     mydict = {
#         'patient': patient,
#         'doctorName': doctor.get_name,
#         'doctorMobile': doctor.mobile,
#         'doctorAddress': doctor.address,
#         'data_Patient': data_Patient,
#         'doctorDepartment': doctor.department,
#         'admitDate': patient.admitDate,
#     }
#     return render(request, 'hospital/patient_dashboard.html', context=mydict)
#
#
# @user_passes_test(is_patient)
# def patient_sending_a_message_view(request):
#     appointmentForm = forms.PatientAppointmentForm()
#     patient = models.Patient.objects.get(user_id=request.user.id)  # for profile picture of patient in sidebar
#     message = None
#     mydict = {'appointmentForm': appointmentForm, 'patient': patient, 'message': message}
#     if request.method == 'POST':
#         appointmentForm = forms.PatientAppointmentForm(request.POST)
#         if appointmentForm.is_valid():
#             print(request.POST.get('doctorId'))
#             desc = request.POST.get('description')
#
#             doctor = models.Doctor.objects.get(user_id=request.POST.get('doctorId'))
#
#             appointment = appointmentForm.save(commit=False)
#             appointment.doctorId = request.POST.get('doctorId')
#             appointment.patientId = request.user.id
#             appointment.doctorName = models.User.objects.get(id=request.POST.get('doctorId')).first_name
#             appointment.patientName = request.user.first_name
#             appointment.status = False
#             appointment.save()
#         return HttpResponseRedirect('patient-view-appointment')
#     return render(request, 'hospital/patient_sending_a_message.html', context=mydict)
