from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('patients/', PatientListCreateView.as_view(), name='patients_list_create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('doctors/', DoctorListCreateView.as_view(), name='doctors_list_create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('mappings/', mapListCreateView.as_view(), name='mapping_list_create'),
    path('mappings/<int:pk>/', mapDetailView.as_view(), name='mapping_detail'),
    path('mappings/<int:patient_id>/', patientDoctorsView.as_view(), name='patient_doctors')
]