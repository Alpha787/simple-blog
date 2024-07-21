from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
# from django.http import HttpResponse
from django.views.generic import TemplateView, View, DetailView, UpdateView, DeleteView, CreateView, ListView
# from django.db import connection
# from django.forms import ModelForm

from .models import Post
from .forms import PostForm

class PostView(View):
  template_name = "posts.html"
  model = Post
  
  # создание поста
  def create(self, request, *args, **kwargs):
    context = {}
    form = PostForm(request.POST or None)
    if form.is_valid():
      form.save()
      
    context['form'] = form
    return render(request, "post_create.html", context)

  
  # получение списка постов
  def get(self, request, *args, **kwargs):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'posts.html', context)

  # обновление поста
  def post(self, request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      form.save()
      return redirect('post_detail', post_id=post_id)
    else:
      context = {'form':form, 'post':post}
      return render(request, 'post_update.html', context)
  
  # удаление поста
  def delete(self, request, *args, **kwargs):
    pass

# Отображение списка постов
class HomeView(ListView):
  model = Post
  context_object_name = "posts"
  paginate_by = 10

  def get_queryset(self) -> QuerySet[Any]:
    queryset = super().get_queryset()
    return queryset.order_by('created_date')
    

  def get_template_names(self):
    if self.request.htmx:
      return "post-list-elements.html"
    return "posts.html"

class PostCreateView(CreateView):
  template_name = "post_create.html"
  model = Post

  def create(self, request, post_id):
    context = {}
    form = PostForm(request.POST or None)
    if form.is_valid():
      form.save()
      
    context['form'] = form
    return render(request, "post_create.html", context)

# Модель для вывода одной статьи. Работает.
class PostDetailView(DetailView):
  template_name = "post_detail.html"
  model = Post
  
  def get(self, request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post':post})

# Модель для метода Update
class PostUpdateView(UpdateView):
  template_name = "post_update.html"
  model = Post

  def put(self, request, post_id):
    context = {}
    obj = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=obj)

    if form.is_valid():
      form.save()
      return HttpResponseRedirect("/"+id)
    
    context["form"] = form
    return render(request, "post_update.html", context)
    
# Модель для метода Delete
class PostDeleteView(DeleteView):
  template_name = "post_delete.html"
  model = Post

  def delete(self, request, post_id):
    context = {}
    obj = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
      obj.delete()
      return HttpResponseRedirect("/")
    return render(request, "delete_view.html", context)