# Generated by Django 2.2.6 on 2020-10-30 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tutorial',
            options={'ordering': ['pub_date']},
        ),
    ]