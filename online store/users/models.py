from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

    
    # def save(self):
    #     super().save()
        
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnall(output_size)
    #         img.save(self.img.path)
    
        
class Archive1(models.Model):
    
    quantity = models.IntegerField(blank=True, null=True)
    item_id = models.BigIntegerField(blank=True, null=True)

   




# Create your models here.
