from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

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

