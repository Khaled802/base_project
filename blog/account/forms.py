
from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, reverse
from .models import CustomUser

class UserRegister(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditProfile(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['picture', 'bio']
