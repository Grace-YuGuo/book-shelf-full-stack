from django.shortcuts import render
# from django.views.generic import TemplateView
# from django.http import HttpResponse
from django.views import generic
from .models import Book

# Create your views here.
# Set up a test view
# def book(request):
#     return HttpResponse('hello book - John')
# class HomePage(TemplateView):
#     """
#     DISPLAY HOMEPAGE
#     """
#     template_name = 'index.html'

# Set up a generic view inherites from generic.ListView class to display all the books
class BookList(generic.ListView):
    queryset= Book.objects.filter(user=1)
    template_name = "book_list.html"