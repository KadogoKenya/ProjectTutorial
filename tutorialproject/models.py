from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = image = CloudinaryField('images/', blank=True)
    content=models.TextField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date=models.DateTimeField(auto_now_add=True)
    authors = models.ManyToManyField(Author)
    Published=models.BooleanField()
    Unpublished=models.BooleanField(default=False)

    def save_tutorial(self):
        self.save()
    
    def delete_tutorial(self):
        self.delete()

    def get_all_tutorials(cls):
        images = cls.objects.all()
        return images

    def __str__(self):
        return self.title

    def get_absolute_url(self):        
        return reverse('index')
    


    
    