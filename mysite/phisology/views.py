from rest_framework import viewsets, generics
from .serializers import *






class ConsultationViewSet(generics.ListAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class RegistrationViewSet(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer