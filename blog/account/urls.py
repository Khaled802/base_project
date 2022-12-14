"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import user_register, user_profile, logout_view, show_profile, my_login
from django.contrib.auth import views
from .forms import UserLoginForm 

urlpatterns = [
    path('register/', user_register, name='account.register'),
    path('profile/', user_profile, name='account.profile'),
    path('logout/', logout_view, name="account.logout"),
    path('show_profile/<int:id>', show_profile, name='account.show_profile'),

      # for block user
    path('C_login/', my_login, name='C_login'),

]