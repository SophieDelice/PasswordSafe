from django.db import models

# Create your models here.
class Password(models.Model):
    StreamingService = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

def __str__(self):
    return self.StreamingService
