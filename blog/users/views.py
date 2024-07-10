from django.shortcuts import render
from django.db import connection
from .models import *

# Create your views here.
def users_list(request):
  users = User.objects.all()
  print(users)
  print(users.query)
  print(connection.queries)
  return render(request, 'users.html', {'users': users})