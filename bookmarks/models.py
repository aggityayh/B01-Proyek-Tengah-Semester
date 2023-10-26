from django.db import models
from django.contrib.auth.models import User
# from caturapp.models import Pustakawan

# Create your models here.
class Book(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    year = models.IntegerField(default=0)

class Bookmark(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=255,default='')
    year = models.IntegerField(default=0)
    