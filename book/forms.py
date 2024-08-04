from django import forms
from .models import Book,Review

class BookForm(forms.ModelForm):
    """
    Create a book form class based on model Book inherited from ModelForm module
    """
    class Meta:
        model = Book
        fields = ('title','author','category','pages','image','description',)

class ReviewForm(forms.ModelForm):
    """
    Create a review form class based on model Review inherited from ModelForm module
    """
    class Meta:
        model = Review
        fields = ('content','rating',)