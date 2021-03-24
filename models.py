from django.db import models

# Create your models here.
class Movie(models.Model):
    title       = models.TextField()
    year        = models.TextField() 
    certificate = models.TextField() 
    duration    = models.TextField() 
    genre       = models.TextField()
    rating      = models.TextField()
    metascore   = models.TextField()
    description = models.TextField()
    director    = models.TextField()
    cast        = models.TextField()
    poster      = models.ImageField(upload_to='images/', default='Photo Unavaliable') 




class User(models.Model):
    
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
