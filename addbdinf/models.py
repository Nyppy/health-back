from django.db import models
from django.contrib.auth.models import User

departments = [('Кардиолог', 'Кардиолог'),
               ('Дерматолог', 'Дерматолог'),
               ('Экстренная мед помощь', 'Экстренная мед помощь'),
               ('Аллерголог/Иммунолог', 'Аллерголог/Иммунолог')
               ]


# Доктор
class Doctor(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_pic/DoctorProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(max_length=50, choices=departments, default='Кардиолог')
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.first_name + " " + self.last_name

    @property
    def get_id(self):
        return self.id

    def __str__(self):
        return "{} ({})".format(self.first_name + " " + self.last_name, self.department)


# Пациент
class Patient(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    snils = models.CharField(max_length=20, null=False)
    # symptoms = models.CharField(max_length=100, null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)  # назначенный врач
    admitDate = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.first_name + " " + self.last_name

    @property
    def get_id(self):
        return self.id

    def __str__(self):
        return self.first_name + " " + self.last_name
        # return self.user.first_name + " (" + self.symptoms + ")"


# Назначение
class Appointment(models.Model):
    patientId = models.PositiveIntegerField(null=True)
    doctorId = models.PositiveIntegerField(null=True)
    patientName = models.CharField(max_length=40, null=True)
    doctorName = models.CharField(max_length=40, null=True)
    appointmentDate = models.DateField(auto_now=True)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False)


class data_Patient(models.Model):
    patientId = models.PositiveIntegerField(null=True)
    pressure = models.CharField(max_length=50)  # давление
    pulse = models.CharField(max_length=50)  # пульс
    date = models.DateField(auto_now=True)  # дата измерения
    time = models.TimeField(auto_now=True)  # Время измерения

    @property
    def get_id(self):
        return self.id


# class formulas_for_calculating_pressure(models.Model):
#     P_c = models.CharField(max_length=50)
#     P_d = models.CharField(max_length=50)
#     ffcp = 0.42 * P_c + 0.58 * P_d