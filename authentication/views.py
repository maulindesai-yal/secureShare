from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.hashers import make_password
from .models import CustomUser

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request,'register.html',{'error':'Passwords do not match'})
        
        if CustomUser.objects.filter(email=email).exists():
            return render(request,'register.html',{'error':'Email already exists'})
        
        
        user = CustomUser(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=make_password(password),
            is_active=True
        )
        user.save()
        return redirect ('login') 
    return render (request,'registration/register.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,email=email,password=password)
        
        print(f"Login attempt: email={email}, authenticated={user is not None}")

        if user is not None:
            login(request,user)
            return redirect ("dashboard")
        else:
            return render (request, 'registration/login.html',{'error':'Invalid credentials'})
    
    return render (request,'registration/login.html')


@login_required(login_url='login')
def dashboard(request):
    return render (request,'home_templates/dashboard.html')

def logout_user(request):
    auth_logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect ('login')
