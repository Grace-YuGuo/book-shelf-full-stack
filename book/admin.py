from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Book,Category,Review
# Register your models here.
# Define a class inheritated from SummernoteModelAdmin to customise the book model layout in admin
@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
    list_display=('title','author','category','created_on')
    search_fields=['title','author']
    list_filter = ('pages',)
    summernote_fields = ('description',)

# admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Review)