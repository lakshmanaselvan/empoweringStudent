from django.contrib import admin
from .models import Registration
from .models import StaffRegistration

# Register your models here.


class registrationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "token", "is_verified")

class staffRegistrationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "token", "is_verified")

admin.site.register(StaffRegistration)
admin.site.register(Registration, registrationAdmin)
