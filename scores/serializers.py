from dataclasses import fields
from rest_framework import serializers
from .models import Project, Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields = '__all__'

