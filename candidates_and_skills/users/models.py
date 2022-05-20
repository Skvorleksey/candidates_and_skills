from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user model with full name"""
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    fathers_name = models.CharField(max_length=50, verbose_name='Отчество')

    def __str__(self):
        return self.username
