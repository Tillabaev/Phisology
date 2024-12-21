from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import *
from .serializer import *
from rest_framework.pagination import PageNumberPagination
from .pagination import ImgPagination


class ImgSimpleList(generics.ListAPIView):
    queryset = Img.objects.all()
    serializer_class = ImgSerializer
    pagination_class = ImgPagination

class ImgReviewAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ImgReviewSerializer


class AboutMeListAPIView(generics.ListAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer


class MainWorldListAPIView(generics.ListAPIView):
    queryset = MainWorld.objects.all()
    serializer_class = MainWorldSerializer




class ConsultationViewSet(generics.ListAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer


class RegistrationViewSet(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer



class My_ServicesViewSet(generics.ListAPIView):
    queryset = My_Services.objects.all()
    serializer_class = My_ServicesSerializer


class ServicesViewSet(generics.RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesDetailSerializer


