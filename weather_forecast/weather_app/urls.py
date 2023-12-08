from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_lookup, name='weather_lookup'),
]