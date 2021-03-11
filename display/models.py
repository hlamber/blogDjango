from django.conf import settings
from django.db import models
from django import forms
from django.utils import timezone
import datetime
# Create your models here.
# class Contact(models.Model):
#     username = models.CharField(max_length=200)
#     mail = models.EmailField(max_length=200)
#     message = models.TextField()
#     date = models.DateTimeField(default=timezone.now)

#     def publish(self):
#         self.date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.mail

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