# Generated by Django 5.0 on 2023-12-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='image',
        ),
        migrations.AddField(
            model_name='animal',
            name='photo',
            field=models.ImageField(default=10, upload_to='animal-photo/'),
            preserve_default=False,
        ),
    ]
