from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Home view for testing purposes
def home(request):
    return render(request, 'home.html')  # Ensure home.html exists in templates

# Profile view for logged-in users
@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

# Registration view to handle new user signups
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('profile')  # Redirect to profile page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# CRUD Operations for Blog Posts

# List all blog posts
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

# Detail view for a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

# Create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # Automatically set the author as the logged-in user
        return super().form_valid(form)

# Update an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensure only the author can update the post
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure the current user is the author of the post

# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')  # Redirect to the list view after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure the current user is the author of the post

