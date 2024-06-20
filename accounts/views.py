# Create your views here.
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
       # Check if passwords match
        if password != confirm_password:
            return render(request, 'register.html', {'error_message': 'Passwords do not match'})
        
        if User.objects.filter(username=username,email=email).exists():
            return render(request, 'register.html', {'error_message': 'Username or email already exists'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        #redirect to login page
        return redirect('login')
    
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login') 

@login_required
def home(request):
    return render(request, 'home.html')