from django.urls import path
from .views import ProfileRegistrationView

urlpatterns = [
    path('register/', ProfileRegistrationView.as_view(), name='profile-registration'),
]