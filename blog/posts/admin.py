from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
# from django.forms import widgets

from posts.models import Post

# Register your models here.

# class PostForm(forms.ModelForm):
#   class Meta:
#     model = Post
#     fields = '__all__'


# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ("id", "image","author","title", "created_date", "published_date")
  list_filter = ("author", "created_date", "published_date")
  date_hierarchy = ("published_date")
  formfield_overrides = {
    # models.CharField: {'widget': TextInput(attrs={'size':20})},
    models.TextField: {"widget": Textarea(attrs={"rows":10, "cols":100})},
  }

admin.site.register(Post, PostAdmin)