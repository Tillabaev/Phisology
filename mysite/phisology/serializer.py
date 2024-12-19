from rest_framework import serializers
from .models import *

class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = ['bio','profession','about_me','photo','back_round_img']


class MainWorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainWorld
        fields = ['profession','main_text','publication','follower','subscription']


class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = ['id','img']


class ImgReviewSerializer(serializers.ModelSerializer):
    photo = ImgSerializer(read_only=True,many=True)
    class Meta:
        model = Review
        fields = ['feedback','phono',]