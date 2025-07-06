from django.contrib import admin

from auth_app.models import Profile

# Register profile model to the admin site
admin.site.register(Profile)
