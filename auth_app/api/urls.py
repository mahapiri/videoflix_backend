from django.urls import path

from auth_app.api.views import ProfileRegistrationView


urlpatterns = [
    path("registration/", ProfileRegistrationView.as_view(), name="registration"),
    # path("login/", ProfilLoginView.as_view(), name="login"),
    # path("email-check/", EmailCheckView.as_view(), name="email-check"),
]