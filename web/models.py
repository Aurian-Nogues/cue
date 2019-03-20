from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
    return f"{self.user} / {self.title} / {self.status}"