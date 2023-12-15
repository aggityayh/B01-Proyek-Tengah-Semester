from django.db import models
from pengelola.models import Buku
from django.contrib.auth.models import User

class Ulasan(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    
    reviewer_name = models.CharField(max_length=255)
    review_text = models.TextField()
    rating = models.IntegerField()  
    review_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
