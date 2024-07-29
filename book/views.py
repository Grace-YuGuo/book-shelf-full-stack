from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
# Set up a test view
# def book(request):
#     return HttpResponse('hello book - John')
class HomePage(TemplateView):
    """
    DISPLAY HOMEPAGE
    """
    template_name = 'index.html'
