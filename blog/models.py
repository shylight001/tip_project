# blog/models.py
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField(blank=True)
    
    payment = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=7,decimal_places=2)
    tips = models.DecimalField(max_digits=6,decimal_places=2,default=0.00)
    last_modified = models.DateTimeField(auto_now=True)  
    time_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
