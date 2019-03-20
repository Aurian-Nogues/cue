from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse


def index(request):
    #if user is not conntected send to login page
    if not request.user.is_authenticated:
        print("here")
        return render(request, "web/login.html", {"message": None})

    return render(request, "web/index.html")

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "web/login.html", {"message": "Invalid credentials."})


def createAccount(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UserCreationForm()

    return render(request, "web/create_account.html", {'form': form})

def logout_view(request):
    logout(request)
    return render(request, "web/login.html", {"message": "Logged out."})

def create_post(request):
    return render(request, "web/create_post.html")

def record_reminder(request):
    #if user is not conntected send to login page
    if not request.user.is_authenticated:
        return render(request, "web/login.html", {"message": None})

    #if request is not a POST, send back to selecting a stock
    if request.method == 'GET':
        return HttpResponseRedirect(reverse("index"))


