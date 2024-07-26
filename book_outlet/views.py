from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book # we are importing the model that we ourselves created within models.py, we will have the same methods that we accessed within the python shell. 
# Create your views here.
def index(request):
    Books = Book.objects.all()
    return render(request,"book_outlet/index.html",{
        "books": Books
    })

def book_detail(request, id):
    # try:
    #     book = Book.objects.get(id=id)
    # except:
    #     raise Http404() or we can do whats below which is an easier shortcut because this is a very common pattern
    book = get_object_or_404(Book,pk=id)
    return render(request, "book_outlet/book_detail.html",{
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })
