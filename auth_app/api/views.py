

from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from auth_app.api.serializers import ProfileRegistrationSerializer, ProfileResponseSerializer
from auth_app.models import Profile


class ProfileRegistrationView(generics.CreateAPIView):
    """
    View to handle user profile registration.
    """
    serializer_class = ProfileRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = self.create_user(serializer.validated_data)
            profile = self.create_profile(user)

            token, _ = Token.objects.get_or_create(user=user)
            response_data = self.create_response_data(token, profile)
            response_serializer = ProfileResponseSerializer(response_data)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError:
            return Response({"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"An internal server error occurred! Errormessage: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create_user(self, validated_data):
        """
        Create a new user with the provided data.
        """
        try:
            created_user = User.objects.create_user(
                username=validated_data["email"],
                email=validated_data["email"],
                password=validated_data["password"]
            )
            return created_user
        except Exception:
            raise Exception()

    def create_profile(self, user):
        """
        Create a new profile associated with the user.
        """
        try:
            new_profile = Profile.objects.create(
                user=user,
            )
            return new_profile
        except Exception:
            user.delete()
            raise Exception()

    def create_response_data(self, token, profile):
        """
        Create the response data structure.
        """
        return {
            "token": token.key,
            "email": profile.user.email,
            "profile_id": profile.id
        }
