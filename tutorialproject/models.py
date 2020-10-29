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

    def save_tutorial(self):
        self.save()
    
    def delete_tutorial(self):
        self.delete()

    def get_all_tutorials(cls):
        images = cls.objects.all()
        return images
    


    
    