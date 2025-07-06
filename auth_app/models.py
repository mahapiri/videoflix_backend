from django.contrib.auth.models import User
from django.db import models


# Create profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    confirmed = models.BooleanField(default=False)

    class Meta: 
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ["user"]

    # returns email of the user
    def __str__(self):
        return self.user.email


