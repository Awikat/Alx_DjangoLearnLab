# relationship_app/views.py

from django.shortcuts import render
from relationship_app.models import Book

def list_books(request):
    """
    View to list all books stored in the database, displaying each title and author.
    """
    books = Book.objects.all()  # Retrieve all books from the database
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)  # Ensure correct template path
