# Generated by Django 3.1.7 on 2021-03-11 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210310_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diplome',
            name='obtained_years',
            field=models.IntegerField(),
        ),
    ]