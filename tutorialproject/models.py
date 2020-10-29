from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField


# Create your models here.

class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = image = CloudinaryField('images/', blank=True)
    content=models.TextField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    Author = models.CharField(max_length=50)
    Published=models.BooleanField()
    Unpublished=models.BooleanField(default=False)

    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.delete()
    
    def __str__(self):
        return self.sitename

    def get_absolute_url(self):        
        return reverse('tutorialpoint')

    
    