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
