from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Define the turple for 5 ratings as one field of review model
RATINGS =  ((1, "Poor"),(2, "Fair"),(3, "Good"),(4, "Very Good"),(5,"Excellent"))

class Category(models.Model):
    """
    Stores a single category entry related to :model:=`Book`
    """
    name = models.CharField(max_length=200,null=False,blank=False)
    
    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    """
    Stores a single book entry related to :modle: =`auth.User` and model:`Category`
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='user_books')
    title = models.CharField(max_length=200,null=False,blank=False, unique=True)
    author = models.CharField(max_length=200,null=False,blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True, related_name='category_books')
    pages = models.IntegerField()
    image = CloudinaryField('image',default ='imageplaceholder')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return f"The book name: {self.title} | category: {self.category} | author: {self.author}"

class Review(models.Model):
    """
    Stores a single comment entry related to :model:=`auth.User` and model:`Book`
    """
    book = models.ForeignKey(Book, on_delete = models.CASCADE, related_name= "book_reviews")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="book_reviewers")
    content = models.TextField()
    rating = models.IntegerField(choices=RATINGS,default=3)
    created_on = models.DateTimeField(auto_now_add= True)
    approved = models.BooleanField(default=False)
  
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Review: {self.content} by {self.user} for {self.book}"