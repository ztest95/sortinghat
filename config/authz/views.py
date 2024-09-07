from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError

from authz.models import User
# Create your views here.

def login_reverse(request):
    return reverse("view_links", kwargs={'user': request.user.username})

def login_user(request):
    if request.method == "POST":
        print(request.POST)
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(login_reverse(request))
        else:
            return render(request, "auth/login.html", {
                "message": "Invalid username and/or password."
            })
        
    elif request.user.is_authenticated:
        # Feat: Might be good to have a bit of a message here before redirecting
        return HttpResponseRedirect(login_reverse(request))
    
    else:
        return render(request, "auth/login.html")

def register_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(login_reverse(request))
    
    elif request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "auth/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except IntegrityError:
            return render(request, "auth/register.html", {
                "message": "Username already taken."
            })
        
        login(request, user)
        return HttpResponseRedirect(login_reverse(request))
    
    else:
        return render(request, "auth/register.html")
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

