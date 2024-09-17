from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import UserRegistrationForm, UserLoginForm

# Create your views here.
# def users_list(request):
#   users = User.objects.all()
#   print(users)
#   print(users.query)
#   print(connection.queries)
#   return render(request, 'users.html', {'users': users})

# Функция регистрации от GPT
def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
  else:
    form = UserRegistrationForm()
  return render(request, 'register.html', {'form': form})

# Функция логина от GPT
def login_view(request):
  if request.method == 'POST':
    form = UserLoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('register')
  else:
    form = UserLoginForm()
  return render(request, 'login.html', {'form':form})

def login_user(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.success(request, ("There Was An Error Logging In, Try Again..."))
      return redirect('login')
  else:
    return render(request, 'registration/login.html', {})