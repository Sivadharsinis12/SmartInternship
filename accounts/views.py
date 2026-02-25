from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Landing Page
def index(request):
    return render(request, 'index.html')


# Login Page
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


# Dashboard Page (Login Required)
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# History Page (Login Required)
@login_required
def history(request):
    return render(request, 'history.html')


def logout_view(request):
    logout(request)
    return redirect('login')