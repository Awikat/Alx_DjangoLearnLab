from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('register/', views.register, name='register'),  # Registration URL
    path('profile/', views.profile, name='profile'),  # Profile URL
]

