from django.db import models

# Create your models here.

class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    content=models.TextField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    Author = models.CharField(max_length=50)
    Published=models.BooleanField(db_index=True, default=False)
    
    
    