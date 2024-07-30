from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0,"Draft"), (1, "Published"))

# Catogory model: CATOGORY = ((0,""))
# RATING model: RATING = ()

# Create your models here.
class Book(models.Model):
    """
    Stores a single book entry related to :modle: =`auth.User`.
    """
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    image = CloudinaryField('image',default ='imageplaceholder')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices = STATUS, default=0)