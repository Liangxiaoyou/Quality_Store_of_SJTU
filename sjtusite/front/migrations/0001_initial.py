# Generated by Django 3.0.4 on 2020-04-25 08:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(4)])),
                ('password', models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(6)])),
                ('telephone', models.CharField(max_length=11)),
            ],
        ),
    ]