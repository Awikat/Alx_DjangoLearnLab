from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.pagination import PageNumberPagination

# Pagination class
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing posts.
    """
    queryset = Post.objects.all().order_by('-created_at')  # Order by newest first
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  # Enable searching by title or content

    def perform_create(self, serializer):
        # Automatically set the author to the logged-in user
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing comments.
    """
    queryset = Comment.objects.all().order_by('-created_at')  # Order by newest first
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        # Automatically set the author to the logged-in user
        serializer.save(author=self.request.user)

