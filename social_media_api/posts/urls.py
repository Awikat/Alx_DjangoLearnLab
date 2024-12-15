from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FeedView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
]

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

# Include the router URLs
urlpatterns = [
    path('', include(router.urls)),
]

