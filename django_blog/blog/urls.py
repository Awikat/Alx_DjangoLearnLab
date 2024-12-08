from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostByTagListView


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    #path('post/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('search/', views.search, name='search'),
    path('tags/<str:tag_name>/', views.TaggedPostListView.as_view(), name='tagged_posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post_by_tag'),
]
