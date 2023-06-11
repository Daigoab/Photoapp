from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Photoblog(models.Model):
    image = CloudinaryField('image', null=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

