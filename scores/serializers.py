from dataclasses import fields
from rest_framework import serializers
from .models import Project, Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model=Project
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    projects = serializers.StringRelatedField(many=True)
    profiles = UserSerializer(read_only = True)

    class Meta:
        model=User
        fields=['username', 'projects','profiles']
