# Generated by Django 5.0 on 2023-12-13 12:57

import phone_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='number',
            field=phone_field.models.PhoneField(default=10, max_length=31, unique=True),
            preserve_default=False,
        ),
    ]