from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    username = models.CharField(max_length=200)
    mail = models.EmailField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title