from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id","username","phone_number", "email", "first_name", "last_name")


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email", "first_name")
        extra_kwargs = {
            "email": {"required": False},
            "first_name": {"required": True},
        }


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id","username","phone_number","password", "email", "first_name", "user_type", "created_at")



class AdminCreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "phone_number", "first_name", "user_type", "password")


class ChangePhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("phone_number",)
