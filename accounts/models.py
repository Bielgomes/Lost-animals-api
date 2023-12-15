from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from phone_field import PhoneField


class NewUserManager(UserManager):
    pass


class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=255)
    phone = PhoneField(unique=True, null=False, blank=False)

    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)

    objects = NewUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
