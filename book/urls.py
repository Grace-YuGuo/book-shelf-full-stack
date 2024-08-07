from django.urls import path, include
from . import views

# Set up urlpatterns for book app
urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('view/<book_id>',views.book_detail, name='book_detail'),
    path('create/', views.create_book, name='create_book'),
    path('edit/<book_id>',views.edit_book,name='edit_book'),
    path('delete/<book_id>',views.delete_book,name='delete_book'),
    path('about/',views.about, name='about'),
    path('search/', views.search, name='search'),
    path('view/edit_review/<review_id>',views.edit_review,name='review_edit',),
    path('view/delete_review/<review_id>',views.delete_review,name='review_delete'),
    path('summernote/', include('django_summernote.urls')),
]