# relationship_app/query_samples.py

from relationship_app.models import Author, Library

def query_books_by_author(author_name):
    """
    Query all books by a specific author using the related manager 'books.all()'.
    """
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()  # Using related manager
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")

def list_books_in_library(library_name):
    """
    List all books in a library using the related manager 'books.all()'.
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Using related manager
        print(f"Books in the '{library_name}' library:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")

def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Access the related librarian directly
        print(f"Librarian for '{library_name}': {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")

# Sample usage:
# query_books_by_author("Author Name")
# list_books_in_library("Library Name")
# retrieve_librarian_for_library("Library Name")
