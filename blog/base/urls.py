
from django.contrib import admin
from django.urls import path, include
from .views import show_about


urlpatterns = [
    path('', show_about, name='about'),
]