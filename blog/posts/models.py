from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  title = models.CharField(max_length=200)
  text = models.TextField(blank=True)
  created_date = models.DateTimeField(auto_created=True)
  published_date = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return self.text