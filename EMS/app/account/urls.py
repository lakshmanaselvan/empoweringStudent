from django.urls import path
from . import views


urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('staffRegistration/', views.staffRegistration, name='staffRegistration'),
    path('verify/<str:token>', views.verify),
    path('login/', views.login, name='login'),
    path('staffLogin/', views.staffLogin, name='staffLogin'),
]