from django.shortcuts import render
from .models import Event
from datetime import date
from .forms import EventForm
# Create your views here.
def home(request):
    return render(request, "home.html", {})

def event(request):
    today = date.today()
    event_list = Event.objects.all()
    return render(request, "event.html", {'event_list': event_list, 'today': today})

def addEvent(request):
    form = EventForm
    return render(request, 'addevents.html', {'form':form})