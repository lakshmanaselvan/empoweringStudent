from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.backends import ModelBackend
from .models import Registration

class RegistrationBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = Registration.objects.get(email=email)
            if user.password == password and user.is_verified:  # Check password and verification status
                return user
        except Registration.DoesNotExist:
            pass

    def get_user(self, user_id):
        try:
            return Registration.objects.get(pk=user_id)
        except Registration.DoesNotExist:
            return None
        
class CustomBackend(ModelBackend):
    def update_last_login(self, request, user):
        # Override the update_last_login method to prevent updating last_login
        pass