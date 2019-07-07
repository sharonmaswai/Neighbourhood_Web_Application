from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField 

# Create your models here.
class Profile(models.Model):
    image=models.ImageField(default='image.png',upload_to='profiles/')
    name=models.CharField(max_length=30)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    phone_number=models.IntegerField()
    bio = HTMLField(max_length=500,default='About me')
    street_name=models.CharField(max_length=30)

    def save_profile(self):
        self.save()
        

    def __str__(self):
        return self.bio
class Concerns(models.Model):
    profile=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True) 
    
    def save_concern(self):
        self.save()
        

    def __str__(self):
        return self.profile  
    