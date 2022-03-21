from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    context = {}
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Your account has been created successfully")
            return HttpResponseRedirect(reverse("data_collector:form_handler"))
        context['form'] = form
        return render(request, "user_auth/register.html", context)
    else:
        form = RegisterForm()
        context["form"] = form
        return render(request, "user_auth/register.html", context)

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.INFO, f"You are logged in as {username}")
            return HttpResponseRedirect(reverse("data_collector:form_handler"))
        else:
            context["error"] = "Invalid username or password"
            return render(request, "user_auth/login.html", context)
    else:
        return render(request, "user_auth/login.html")

def user_logout(request):
        logout(request)
        messages.add_message(request, messages.INFO, "You have logged out successfully")
        return HttpResponseRedirect(reverse("user_auth:login"))

