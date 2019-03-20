from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import Message


def index(request):
    #if user is not conntected send to login page
    if not request.user.is_authenticated:
        print("here")
        return render(request, "web/login.html", {"message": None})

        #load  user specific reminders

    user = request.user
    reminders = Message.objects.all().filter(user=user)
    
    context = {
        "reminders":reminders,
    }

    return render(request, "web/index.html", context)

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


#receives Ajax requests when new entry is created and writes them in database
def record_reminder(request):
    #if user is not conntected send to login page
    if not request.user.is_authenticated:
        return render(request, "web/login.html", {"message": None})

    #if request is not a POST, send back to selecting a stock
    if request.method == 'GET':
        return HttpResponseRedirect(reverse("index"))

    if request.is_ajax() and request.POST:
        user = request.user
        title = request.POST.get('title')
        status = request.POST.get('status')
        url = "test_url"

        entry = Message(user=user, title=title, status=status,url=url)
        entry.save()

        return HttpResponseRedirect(reverse("index"))

#receives Ajax request to change reminder status
def change_status(request):
    #if user is not conntected send to login page
    if not request.user.is_authenticated:
        return render(request, "web/login.html", {"message": None})

    #if request is not a POST, send back to selecting a stock
    if request.method == 'GET':
        return HttpResponseRedirect(reverse("index"))

    if request.is_ajax() and request.POST:
        id = request.POST.get('id')
        status = request.POST.get('status')

        message = reminders = Message.objects.all().get(id=id)
        message.status = status
        message.save()

        return HttpResponseRedirect(reverse("index"))