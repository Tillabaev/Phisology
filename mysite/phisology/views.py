from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *


class AboutMeListAPIView(generics.ListAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer


class MainWorldListAPIView(generics.ListAPIView):
    queryset = MainWorld.objects.all()
    serializer_class = MainWorldSerializer


class ImgReviewAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ImgReviewSerializer


class ConsultationViewSet(generics.ListAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class RegistrationViewSet(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
