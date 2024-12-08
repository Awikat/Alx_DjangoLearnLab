from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('posts/', views.PostListView.as_view(), name='post_list'),  # List posts
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # Post detail
    path('posts/new/', views.PostCreateView.as_view(), name='post_create'),  # Create post
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),  # Edit post
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Delete post
]
]

