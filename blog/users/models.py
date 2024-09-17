from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField(unique=True, null=True, blank=True)
  surname = models.CharField(max_length=50)
  
  def __str__(self) -> str:
    return self.name