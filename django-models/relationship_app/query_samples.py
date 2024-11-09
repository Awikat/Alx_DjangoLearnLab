# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """
    Query all books by a specific author using objects.filter().
    """
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")

def list_books_in_library(library_name):
    """
    List all books in a library using objects.filter().
    """
    try:
        library = Library.objects.get(name=library_name)
        books = Book.objects.filter(libraries=library)
        print(f"Books in the '{library_name}' library:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")

def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library using objects.filter().
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.filter(library=library).first()
        if librarian:
            print(f"Librarian for '{library_name}': {librarian.name}")
        else:
            print(f"No librarian assigned to '{library_name}'.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")

# Sample usage:
# query_books_by_author("Author Name")
# list_books_in_library("Library Name")
# retrieve_librarian_for_library("Library Name")
