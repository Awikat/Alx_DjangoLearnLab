from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book
from .forms import ExampleForm

def search_books(request):
    form = ExampleForm(request.GET)
    books = []
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)  # Safe query using ORM
    return render(request, 'bookshelf/search_results.html', {'form': form, 'books': books})

@permission_required('books.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/list_books.html', {'books': books})

@permission_required('books.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')

        if title and author and published_date:
            Book.objects.create(title=title, author=author, published_date=published_date)
            return redirect('list_books')  # Redirect to the list_books view
    return render(request, 'books/create_book.html')

@permission_required('books.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.save()
        return redirect('list_books')  # Redirect to the list_books view
    return render(request, 'books/edit_book.html', {'book': book})

@permission_required('books.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')  # Redirect to the list_books view
    return render(request, 'books/delete_book.html', {'book': book})
