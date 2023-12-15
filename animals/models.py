from django.db import models

from accounts.models import User
from .choices import GenderTextChoices


class Animal(models.Model):
    name = models.CharField(max_length=50)
    gender = models.TextField(choices=GenderTextChoices.choices)
    date_of_birth = models.DateTimeField()
    adoption = models.BooleanField(default=False)

    serial_number = models.CharField(unique=True, max_length=6)

    photo = models.ImageField(upload_to='animal-photo/')

    breed = models.ForeignKey('Breed', models.PROTECT)
    type = models.ForeignKey('Type', models.PROTECT)

    tutor = models.ForeignKey(User, models.CASCADE)

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"


class Breed(models.Model):
    name = models.CharField(max_length=25)
    type = models.ForeignKey('Type', models.PROTECT)

    class Meta:
        verbose_name = "Raça"
        verbose_name_plural = "Raças"


class Type(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name = "Espécie"
        verbose_name_plural = "Espécies"