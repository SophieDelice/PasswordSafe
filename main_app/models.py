from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Passcard(models.Model):
    StreamingService = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
         return self.StreamingService

    def get_absolute_url(self):
         return reverse('passwords_detail', kwargs={'password_id': self.id})

