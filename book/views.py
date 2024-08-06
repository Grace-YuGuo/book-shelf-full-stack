from django.shortcuts import render,get_object_or_404,reverse, redirect
# from django.views.generic import TemplateView
# from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q
from .forms import BookForm, ReviewForm
from .models import Book,Review

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
    paginate_by = 6

# def is_creator_or_superuser(view_func):
#     """
#     Define a function to decide if the user is the book creator or the superuser
#     """
#     def wrapper(request, *args, **kwargs):
#         book = get_object_or_404(Book, pk=kwargs['pk'])
#         if book_user == request.user or request.user.is_superuser:
#             return view_func(request,*args,**kwargs)
#         else:
#             messages.error(request,'You cannot modify an article you did not create!')
#             return redirect('home')


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
    reviews = retrieved_book.book_reviews.all()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.book = retrieved_book
            review.save()
            messages.add_message(request,messages.SUCCESS,'Review submitted and awaiting approval')
    review_form = ReviewForm()
    review_count =retrieved_book.book_reviews.filter(approved=True).count()

    return render(request,"book/book_detail.html",{"book": retrieved_book, "reviews":reviews,"review_count":review_count, "review_form":review_form,},)

@login_required
def create_book(request):
    """
    Create an individual instance : model:`book.Book`.
    
    **Context**
    ``book``
        An instance of : model:`book.Book`.

    **Template:**
    :template:`book/create_book.html` or redirect 'home' for POST method
    """
    if request.method =='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user= request.user
            book.approved=False
            book.save()
            messages.success(request,'Book submitted and awaiting approval')
            return redirect('home')
        else:
            messages.error(request,f"{f.errors}")
            return redirect("create_book")
    else:
        # handle a GET request
        form = BookForm()
        return render(request, 'book/create_book.html',{"form":form})

@login_required
def edit_book(request,book_id):
    """
    Edit an individual instance of specific book_id : model:`book.Book`.
    
    **Context**
    ``book``
        An instance of : model:`book.Book` with specific book_id passed through from url.

    **Template:**
    :template:`book/edit_book.html` or redirect 'home' for POST method
    """
    retrieved_book = get_object_or_404(Book, id=book_id)

    if not request.user == retrieved_book.user and not request.user.is_superuser:
        messages.error(request,'You cannot update an article you did not create!')
        return redirect('home')

    if request.method =='POST':
        form = BookForm(request.POST,instance=retrieved_book)
        if form.is_valid():
            book = form.save(commit=False)
            book.user= request.user
            book.approved=False
            book.save()
            messages.success(request,'Book updating submitted and awaiting approval')
            return redirect('home')
        else:
            messages.error(request,f"{f.errors}")
            return redirect("edit_book")
    else:
        # handle a GET request
        form = BookForm(instance=retrieved_book)
        return render(request, 'book/edit_book.html',{"form":form})

@login_required
def delete_book(request,book_id):
    """
    Delete an individual instance of specific book_id : model:`book.Book`.
    
    **Context**
    ``book``
        An instance of : model:`book.Book` with specific book_id passed through from url.

    **Template:**
    :template:`book/delete_book.html` or redirect 'home' for POST method
    """
    retrieved_book = get_object_or_404(Book, id=book_id)

    if not request.user == retrieved_book.user and not request.user.is_superuser:
        messages.error(request,'You cannot delete an article you did not create!')
        return redirect('home')

    if request.method =='POST':
        retrieved_book.delete()
        messages.success(request,'Your book was deleted!')
        return redirect('home')
    else:
        # handle a GET request
        return render(request, 'book/delete_book.html',{"book":retrieved_book})

@login_required
def edit_review(request,review_id):
    """
    Edit an individual instance of specific review_id of specific book_id : model:`book.Book` and `book.Review`
    
    **Context**
    ``review``
    An instance of : model:`book.Review` with specific review_id and book_id passed through from url.

    **Template:**
    :template: `book/book_detail.html`
    """
    if request.method == "POST":
        review = get_object_or_404(Review, id=review_id)
        # book = get_object_or_404(Book, id=review.book.id)
        
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.user == request.user:
            # review = review_form.save(commit=False)
            # review.book = book
            # review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated! Await approval.')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')

    return HttpResponseRedirect(reverse('book_detail', args=[review.book.id]))



@login_required
def delete_review(request, review_id):
    """
    Delete an individual instance of specific review_id of specific book_id : model:`book.Book` and `book.Review`
    
    **Context**
    ``review``
    An instance of : model:`book.Review` with specific review_id passed through from url.

    **Template:**
    :template: `book/book_detail.html`
    """
    try:
        review = get_object_or_404(Review, id=review_id)
    except Review.DoesNotExist:
        return HttpResponse("Review not found", status=404)

    if review.user == request.user:
        # Perform the delete operation
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')
    
    return HttpResponseRedirect(reverse('book_detail', args=[review.book.id]))  # Redirect to a list of reviews or another appropriate page


def about(request):
    return render(request, 'book/about.html')

def search(request):
    query = request.GET.get('query', '')
    results = []
    if query:
        results = Book.objects.filter(Q(author=query)|Q(title=query))
    
    return render(request, 'book/index.html', {'results': results, 'query': query})