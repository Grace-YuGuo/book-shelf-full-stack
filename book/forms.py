from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Book,Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'category', 'pages', 'image', 'description',)
        widgets = {
            'description': SummernoteWidget(),
        }
      

class ReviewForm(forms.ModelForm):
    """
    Create a review form class based on model Review inherited from ModelForm module
    """
    class Meta:
        model = Review
        fields = ('content','rating',)