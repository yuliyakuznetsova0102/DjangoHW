from django.contrib.auth.models import AbstractUser
from  django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    username = None  # Убираем поле username
    email = models.EmailField(_('email address'), unique=True)  # Email как уникальное поле
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Аватар
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Номер телефона
    country = models.CharField(max_length=100, blank=True, null=True)  # Страна

    USERNAME_FIELD = 'email'  # Используем email для авторизации
    REQUIRED_FIELDS = []  # Убираем username из обязательных полей

    def __str__(self):
        return self.emaill