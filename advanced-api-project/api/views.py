from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookGenericAPIView(generics.GenericAPIView):
    """
    Generic API view for managing books with additional functionalities:
    - Permission checks
    - Filtering, searching, and ordering
    """
    # Define authentication mechanisms
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    # Specify the queryset
    queryset = Book.objects.all()

    # Define the serializer class
    serializer_class = BookSerializer

    # Permission classes
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Backends for filtering, searching, and ordering
    filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Fields to allow exact-match filtering
    filterset_fields = ['publication_year', 'author__name']

    # Fields to allow searching
    search_fields = ['title', 'author__name']

    # Fields to allow ordering
    ordering_fields = ['title', 'publication_year']

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve a list of books.

        Features:
        - Applies filtering, searching, and ordering
        - Returns serialized data
        """
        # Apply filtering, searching, and ordering to the queryset
        books = self.filter_queryset(self.get_queryset())

        # Serialize the filtered queryset
        serializer = self.get_serializer(books, many=True)

        # Return the serialized data in the response
        return Response(serializer.data)


class BookListView(generics.ListAPIView):
    """
    API view to list books with support for filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filtering, searching, and ordering backends
    filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Fields available for filtering
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Fields available for searching
    search_fields = ['title', 'author__name']

    # Fields available for ordering
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']


class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve details of a specific book.
    - Allows read-only access for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.
    - Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users


class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.
    - Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users


class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a book.
    - Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users
