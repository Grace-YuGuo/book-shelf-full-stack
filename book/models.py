from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

CATEGORY = ((0,"Literary fiction"), (1,"Science fiction"), (2,"Horror"), (3,"Romance")
, (4,"Mystery"), (5,"Fantasy"), (6,"Poetry")
, (7,"Drama"), (8,"Humor"), (9,"History")
, (10,"Photography"), (11,"Biography"), (12,"Art")
, (13,"Travel"),(14,"Other")
)

# Create your models here.
class Book(models.Model):
    """
    Stores a single book entry related to :modle: =`auth.User`
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200,null=False,blank=False, unique=True)
    author = models.CharField(max_length=200,null=False,blank=False)
    category = models.IntegerField(choices = CATEGORY, default= 0, null=False, blank=False)
    pages = models.IntegerField()
    image = CloudinaryField('image',default ='imageplaceholder')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return f"{self.title} with category of {self.category} written by{self.author}"