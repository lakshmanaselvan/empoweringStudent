from django.contrib import admin
from .models import Event
from .models import Categorie
from .models import Venue

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    def start_time(self, obj):
        return obj.startTime.strftime("%H:%M:%S")
    def end_time(self, obj):
        return obj.endTime.strftime("%H:%M:%S")
    list_display = ("name","description", "start_time", "end_time", "startDate", "endDate", "participation")

admin.site.register(Event, EventAdmin)
admin.site.register(Categorie)
admin.site.register(Venue)
