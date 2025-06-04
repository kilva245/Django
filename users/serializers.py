from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(Write_only = True, required = True, validators=[validate_password])
    password2 = serializers.CharField(Write_only = True, required = True)