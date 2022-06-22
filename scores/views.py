from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import Registration, LoginForm, SubmitForm, ProfileEditForm
from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Project, Profile, Ratings
from .serializers import ProjectSerializer, ProfileSerializer
from rest_framework.decorators import api_view

# Views.


def register_request(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You are Successfully Registered. Proceed to Login")
            return redirect("login")
        messages.error(
            request, "Registration Failed. Use a Strong Password and Fill all the Fields")
    form = Registration()
    return render(request, template_name="auth/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "You Entered Wrong Username or Password")
            return redirect('login')
    form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, 'auth/login.html', context=context)


