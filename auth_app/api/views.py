from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializers import ProfileRegistrationSerializer


class ProfileRegistrationView(APIView):
    """
    Improved ProfileRegistrationView that returns detailed serializer validation errors.
    
    Changes made according to the problem statement:
    1. Uses serializer.is_valid(raise_exception=True) to automatically raise detailed ValidationError exceptions
    2. Removed the custom validated_serializer method that obscured error details
    3. Updated create method to catch ValidationError as ve and return ve.detail in response
    4. Returns field-level validation errors preserving serializer error details
    """
    
    def create(self, request, *args, **kwargs):
        """
        Improved create method that returns detailed validation errors.
        """
        try:
            serializer = ProfileRegistrationSerializer(data=request.data)
            # Use raise_exception=True to automatically raise detailed ValidationError exceptions
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({
                'message': 'User created successfully',
                'user_id': user.id
            }, status=status.HTTP_201_CREATED)
        except ValidationError as ve:
            # Return the detailed validation errors from the serializer
            return Response(
                ve.detail, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": "An error occurred during registration"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)