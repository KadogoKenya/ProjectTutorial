# Generated by Django 2.2.6 on 2020-10-29 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialproject', '0007_auto_20201029_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='url',
            field=models.CharField(default='www.github.com', max_length=50),
        ),
    ]