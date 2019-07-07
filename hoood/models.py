from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField 

# Create your models here.
class Profile(models.Model):
    image=models.ImageField(default='image.png',upload_to='profiles/')
    first_name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    phone_number=models.IntegerField()
    bio = HTMLField(max_length=500,default='About me')
    street_name=models.CharField(max_length=30)

    def __str__(self):
        return self.surname
class Concerns(models.Model):
    profile=models.ForeignKey(Profile)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.profile  
    