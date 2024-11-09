# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from relationship_app.models import Book, Library

# Function-based view to list all books
def list_books(request):
    """
    View to list all books stored in the database, displaying each title and author.
    """
    books = Book.objects.select_related('author').all()  # Optimize by fetching related author data
    context = {
        'books': books
    }
    return render(request, 'relationship_app/book_list.html', context)


# Class-based view to display library details
class LibraryDetailView(DetailView):
    """
    View to display details for a specific library, listing all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
