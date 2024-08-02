from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    Create a book form class based on model Book inherited from ModelForm module
    """
    class Meta:
        model = Book
        fields = ('title','author','category','pages','image','description',)