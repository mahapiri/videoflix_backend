
from django.contrib.auth.models import User
from rest_framework import serializers


class ProfileRegistrationSerializer(serializers.Serializer):
    """
    Serializer for user registration.

    Handles validation of user registration data including password matching and email uniqueness.
    """
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(write_only=True, min_length=8)
    repeated_password = serializers.CharField(write_only=True, min_length=8)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "This email address already exist!")
        return value

    def validate(self, data):
        if data.get("password") != data.get("repeated_password"):
            raise serializers.ValidationError({
                "passwords": "The passwords do not match!"
            })
        data.pop("repeated_password")
        return data


class ProfileResponseSerializer(serializers.Serializer):
    """
    Serializer for user profile response after registration or login.

    Returns authentication token and basic user information.

    """
    token = serializers.CharField()
    email = serializers.EmailField()
    profile_id = serializers.IntegerField()
