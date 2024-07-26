from django.shortcuts import render
from .models import Book # we are importing the model that we ourselves created within models.py, we will have the same methods that we accessed within the python shell. 
# Create your views here.
def index(request):
    Books = Book.objects.all()
    return render(request,"book_outlet/index.html",{
        "books": Books
    })