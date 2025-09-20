from rest_framework import generics,permissions
from .serializer import *
from rest_framework.permissions import AllowAny


class RegisterView(generics.CreateAPIView):
    serializer_class = registerSerializer
    permission_classes = [AllowAny]


class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = patientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # return Patient.objects.filter(user=self.request.user)
        return Patient.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = patientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # return Patient.objects.filter(user=self.request.user)
        return Patient.objects.all()


class DoctorListCreateView(generics.ListCreateAPIView):
    serializer_class = doctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # return Doctor.objects.filter(user=self.request.user)
        return Doctor.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = doctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # return Doctor.objects.filter(user=self.request.user)
        return Doctor.objects.all()

class mapListCreateView(generics.ListCreateAPIView):
    serializer_class = patientDoctorMapSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return patientDoctorMapping.objects.all()  

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  


class mapDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = patientDoctorMapSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return patientDoctorMapping.objects.all()


class patientDoctorsView(generics.ListAPIView):
    serializer_class = patientDoctorMapSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return patientDoctorMapping.objects.filter(patient_id=patient_id)




    



