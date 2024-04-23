from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate,login,logout
from django.core.mail import EmailMessage
from django.conf import settings
# from .utils import TokenGenerator, generate_token

# Create your views here.
def signUp(request):
    if request.method == "POST" :
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        confirm_password = request.POST.get("pass2")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, "authentication/signup.html")
        
         # Check if a user with this email already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, "A user with this email already exists.")
            return redirect('/authCart/login')
        
        user = User.objects.create_user(email, email, password)
        messages.success(request, "Account created successfully")
        user.is_active = True
        user.save()       

    return render(request, "authentication/signup.html")


def handle_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials or User do not exist.")
            return redirect("/authCart/login")
    return render(request, "authentication/login.html")


def handle_logout(request):
    return render(request, "authentication/logout.html")