from django.db import models
from django.urls import reverse

# Create your models here.
class Password(models.Model):
    StreamingService = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

def __str__(self):
    return self.StreamingService

# def get_absolute_urp(self):
#     return reverse('passwords_detail', kwargs={'password_id': self.id})

#    def get_absolute_url(self):
#         return reverse ('books_detail', kwargs={'book_id': self.id})