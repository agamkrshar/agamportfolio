from django.db import models
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    text = models.TextField(max_length=2000)

    def __str__(self):
        return self.first_name
