from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  title = models.CharField(max_length=200)
  image = models.ImageField(upload_to='images/', null=True, blank=True)
  text = models.TextField(blank=True)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(default=timezone.now)

  def __str__(self) -> str:
    return self.text