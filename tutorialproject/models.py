from django.db import models

# Create your models here.

class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    iimage = models.ImageField(upload_to='images/', blank=True)
    content=models
    pub_date = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    author_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, default='1')
    link = models.URLField()
    country = CountryField(blank_label='(select country)', default='Kenya')
