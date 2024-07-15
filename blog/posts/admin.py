from django.contrib import admin
from posts.models import Post
# Register your models here.

# class PostForm(forms.ModelForm):
#   class Meta:
#     model = Post
#     fields = '__all__'


# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ("id", "author","title", "text", "created_date", "published_date")
  list_filter = ("author", "created_date", "published_date")
  date_hierarchy = ("published_date")
  

admin.site.register(Post, PostAdmin)