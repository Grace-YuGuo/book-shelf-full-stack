from django.shortcuts import render,get_object_or_404
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
    queryset= Book.objects.filter(approved=1)
    template_name = "book/index.html"
    paginate_by = 4

def book_detail(request, book_id):
    """
    Display an individual : model:`book.Book`.
    
    **Context**
    ``book``
        An instance of : model:`book.Book`.
    ``reviews``
        All approved reviews related to the book.
    ``reviews_count``
        A count of approved reviews related to the book.
    ``review_form``
        An instance of :form:`book.ReviewsForm`.

    **Template:**
    :template:`book/book_detail.html`
    """
    retrieved_book = get_object_or_404(Book, id=book_id)
    return render(request,"book/book_detail.html",{"book": retrieved_book,},)

