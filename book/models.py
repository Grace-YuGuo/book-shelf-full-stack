from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Stores a single category entry related to :model:=`Book`
    """
    name = models.CharField(max_length=200,null=False,blank=False)
    
    def __str__(self):
        return f"{self.name}"


# Create your models here.
class Book(models.Model):
    """
    Stores a single book entry related to :modle: =`auth.User` and model:`category`
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200,null=False,blank=False, unique=True)
    author = models.CharField(max_length=200,null=False,blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    pages = models.IntegerField()
    image = CloudinaryField('image',default ='imageplaceholder')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return f"{self.title} | category: {self.category} | author: {self.author}"