from django.contrib import admin
from posts.models import Post
from django import forms
# Register your models here.

# class PostForm(forms.ModelForm):
#   class Meta:
#     model = Post
#     fields = '__all__'

admin.site.register(Post)