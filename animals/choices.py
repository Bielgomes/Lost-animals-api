from django.db import models


class LostAnimalsTextChoices(models.TextChoices):
    pass


class GenderTextChoices(LostAnimalsTextChoices):
    MALE = 'male', 'Macho'
    FEMALE = 'female', 'Fêmea'
