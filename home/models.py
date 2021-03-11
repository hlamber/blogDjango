from django.conf import settings
from django.db import models
from django import forms
from django.utils import timezone
import datetime

class InfosPerso(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone =  models.CharField(max_length=200)
    birthday = models.DateField()
    hobbies = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name + " " + self.last_name

LEVEL_CHOICES = [
    ('ELEMENTAIRE', 'Elementaire'),
    ('INDEPENDANT', 'Indépendant'),
    ('EXPERIMENTE', 'Expérimenté'),
]

class Langue(models.Model):
    id_infosPerso = models.ForeignKey(InfosPerso, null=True, on_delete=models.CASCADE)
    langue = models.CharField(max_length=200)
    level = models.CharField(max_length=12, choices=LEVEL_CHOICES)

    def __str__(self):
        return '{} {}'.format(self.id_infosPerso, self.langue)

class Skill(models.Model):
    id_infosPerso = models.ForeignKey(InfosPerso, null=True, on_delete=models.CASCADE)
    skill = models.CharField(max_length=200)
    level = models.CharField(max_length=12, choices=LEVEL_CHOICES)

    def __str__(self):
        return '{} {}'.format(self.id_infosPerso, self.skill)


class Experience(models.Model):
    id_infosPerso = models.ForeignKey(InfosPerso, null=True, on_delete=models.CASCADE)
    experience_name = models.CharField(max_length=200)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=200)

    def __str__(self):
        return '{} {}'.format(self.id_infosPerso, self.experience_name)

MENTION_CHOICES = [
    ('TRES BIEN', 'Très bien'),
    ('BIEN', 'Bien'),
    ('ASSEZ BIEN', 'Assez bien'),
    ('SANS', 'Sans'),
]


class Diplome(models.Model):
    id_infosPerso = models.ForeignKey(InfosPerso, null=True, on_delete=models.CASCADE)
    degree_name = models.CharField(max_length=200)
    mention = models.CharField(max_length=30, choices=MENTION_CHOICES)
    institution = models.CharField(max_length=200)
    obtained_years = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.id_infosPerso, self.degree_name)