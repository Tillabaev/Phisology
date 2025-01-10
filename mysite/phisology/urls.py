from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/',MainWorldListAPIView.as_view(),name = 'main_world'),

    path('me/<int:pk>/',AboutMeListAPIView.as_view(),name = 'about_me'),

    path('review/<int:pk>/',ImgReviewAPIView.as_view(),name = 'review'),

    path('consultation/<int:pk>/', ConsultationViewSet.as_view(), name='consultation-list'),

    path('registration/<int:pk>/', RegistrationViewSet.as_view(), name='registration-create'),


    path('my_services/', My_ServicesViewSet.as_view(), name='my-services'),

    path('services/', ServicesViewSet.as_view(), name='service-list'),

    path('services/<int:pk>/', ServicesDetailAPIView.as_view(), name='service-detail'),

    path('img/',ImgSimpleList.as_view(),name = 'img'),

    path('questions/',QuestionsListAPIView.as_view(),name = 'questions'),

    path('public_offer/',Public_offerList.as_view(),name  = 'public_offer'),

    path('public_offer_text/',Public_offerTextList.as_view(),name = 'public_offer_text'),

    path('safety/',SafetyList.as_view(),name = 'safety'),

    path('safety/',SafetyMainListAPIView.as_view(),name = 'safety_class'),
]
