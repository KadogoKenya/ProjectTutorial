# Generated by Django 2.2.6 on 2020-10-29 08:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_pics'),
        ),
    ]