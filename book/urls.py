from django.urls import path
from . import views

# Set up urlpatterns for book app
urlpatterns = [
    path('', views.book, name='book'),
]