# Generated by Django 3.1.7 on 2021-03-11 13:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_merge_20210311_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infosperso',
            name='phone',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Numéro de téléphone incorrect', regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]