from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Set up a test view
def book(request):
    return HttpResponse('hello book - John')
