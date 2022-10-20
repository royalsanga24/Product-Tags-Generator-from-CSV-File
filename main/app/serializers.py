from dataclasses import field, fields
from rest_framework import serializers
from .models import *

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = uploadedFile
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = resultResponse
        fields = '__all__'
