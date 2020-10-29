# Generated by Django 2.2.6 on 2020-10-28 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('content', models.TextField(max_length=255)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('Author', models.CharField(max_length=50)),
                ('Published', models.BooleanField(db_index=True, default=False)),
            ],
        ),
    ]
