# Generated by Django 3.1.7 on 2021-03-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20210311_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infosperso',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
