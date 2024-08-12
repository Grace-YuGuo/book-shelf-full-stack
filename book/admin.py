from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Book, Category, Review

# Define a class inheritated from SummernoteModelAdmin to
# customise the book model layout in admin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
    """
    This class defines the display list, search fields, filtering list and
    summernote filed in admin for Book model.
    """
    list_display = ('title', 'author', 'category', 'created_on')
    search_fields = ['title', 'author']
    list_filter = ('approved', 'category')
    summernote_fields = ('description', )


# Register model of Category and Review into admin
admin.site.register(Category)

# Define a class inheritated from SummernoteModelAdmin to
# customise the book model filtering in admin


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """
    This class defines the  filtering list  in admin for Review model.
    """
    list_filter = ('approved',)
