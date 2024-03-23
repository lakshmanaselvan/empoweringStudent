from django.db import models



# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    is_verified = models.BooleanField(default = False)
    token = models.CharField(max_length=100, default=None)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    has_module_perms = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    def has_module_perms(self):
        return self.has_module_perms

class StaffRegistration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    is_verified = models.BooleanField(default = False)
    token = models.CharField(max_length=100, default = None)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name