from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import *

# Create your views here.
# главная страница блога
def post_list(request):
  posts = Post.objects.all()
  print(posts)
  print(posts.query)
  print(connection.queries)
  return render(request, 'posts.html', {'posts':posts})

# страница отдельной статьи
# def post(request):
#   pass

# # регистрация пользователя
# def register_page(request):
#   pass

# # административная панель
# def admin_panel():
#   pass