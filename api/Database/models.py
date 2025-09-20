# api/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=10,null=False,blank=False,unique = True,validators=[RegexValidator(regex=r'^\d{10}$', message='Phone number must be exactly 10 digits')])
    address = models.TextField()
    email = models.EmailField(unique=True,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(unique=True,null=False,blank=False)
    phone = models.CharField(max_length=10,unique = True,null=False,blank=False,validators=[RegexValidator(regex=r'^\d{10}$', message='Phone number must be exactly 10 digits')])
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class patientDoctorMapping(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='doctor_mappings')
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='patient_mappings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('patient', 'doctor')  

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
