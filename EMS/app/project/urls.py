from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('events/', views.event, name="events"),
    path('addevent/',views.addEvent, name="addevent")
]