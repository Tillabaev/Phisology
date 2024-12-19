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



class Consultation_KeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation_Keys
        fields = ['id', 'keys']



class ConsultationSerializer(serializers.ModelSerializer):
    con_keys = Consultation_KeysSerializer(many=True)
    class Meta:
        model = Consultation
        fields = ['id', 'title', 'description', 'con_keys', 'duration', 'format', 'feedback', 'price']


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'first_name', 'last_name', 'email', 'number', 'country']