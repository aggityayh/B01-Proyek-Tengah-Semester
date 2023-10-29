from django.db import models

class Book(models.Model):
    title = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    subjects = models.TextField(null=True, blank=True)
