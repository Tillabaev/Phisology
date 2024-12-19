from rest_framework import serializers
from .models import *



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