from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import *


router = routers.DefaultRouter()



urlpatterns = [
    path('', include(router.urls)),
    path('consultation', ConsultationViewSet.as_view(), name='consultation-list'),
    path('registration', RegistrationViewSet.as_view(), name='registration-create'),

]