# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view for listing books (already created)
def list_books(request):
    """
    View to list all books stored in the database, displaying each title and author.
    """
    books = Book.objects.all()  # Retrieve all books from the database
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)  # Ensure correct template path

# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    """
    View to display details for a specific library, listing all books available in that library.
    """
    model = Library  # The model for the view is Library
    template_name = 'relationship_app/library_detail.html'  # Define the template to use
    context_object_name = 'library'  # The object will be accessible as 'library' in the template

    def get_context_data(self, **kwargs):
        """
        Override the default context to add all books for the current library.
        """
        context = super().get_context_data(**kwargs)
        # Get all books related to the library (many-to-many relationship)
        context['books'] = self.object.books.all()  # 'self.object' is the current library instance
        return context
