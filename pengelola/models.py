from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Buku(models.Model):
    text_number = models.IntegerField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=255 ,null=True, blank=True)
    first_name = models.CharField(max_length=255 ,null=True, blank=True)
    last_name = models.CharField(max_length=255 ,null=True, blank=True)
    year = models.CharField(max_length=255 ,null=True, blank=True)
    subjects = models.TextField(null=True, blank=True)
    bookshelves = models.TextField(null=True, blank=True, default="-")

