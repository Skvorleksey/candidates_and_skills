from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.db import models


class CustomUserCreationForm(UserCreationForm):
    """Create custom user"""
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'surname', 'fathers_name')


class CustomUserChangeForm(UserChangeForm):
    """Change custom user data"""
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ('username', 'email')