from django.urls import path
from .views import *

urlpatterns = [
    path('',MainWorldListAPIView.as_view(),name = 'main_world'),

    path('me/',AboutMeListAPIView.as_view(),name = 'about_me'),

    path('review/',ImgReviewAPIView.as_view(),name = 'review'),

]

