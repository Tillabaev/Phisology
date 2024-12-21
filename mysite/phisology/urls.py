from django.urls import path
from .views import *

urlpatterns = [
    path('',MainWorldListAPIView.as_view(),name = 'main_world'),

    path('me/',AboutMeListAPIView.as_view(),name = 'about_me'),

    path('review/',ImgReviewAPIView.as_view(),name = 'review'),

    path('consultation/', ConsultationViewSet.as_view(), name='consultation-list'),

    path('registration/', RegistrationViewSet.as_view(), name='registration-create'),

    path('img/',ImgSimpleList.as_view(),name = 'img'),



    path('my_services/', My_ServicesViewSet.as_view(), name='my-services'),

    path('services/<int:pk>/', ServicesViewSet.as_view(), name='service-detail'),


]
