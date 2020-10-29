from django.db import models
import cloudinary
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = image = CloudinaryField('images/', blank=True)
    content=models.HTMLField()
    Author = models.ForeignKey(User, default='kate')
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    Published=models.BooleanField()
    Unpublished=models.BooleanField(default=False)
    url = models.CharField(max_length=50, default='www.github.com')
    # submitted = models.DateTimeField(auto_now_add=True, default='2000-01-02')

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
        return reverse('tutorialpoint')

    @classmethod
    def search_by_title(cls,search_term):
        tutorials = cls.objects.filter(title__icontains=search_term)
        return tutorials
    


    
    