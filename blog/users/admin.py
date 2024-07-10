from django.contrib import admin
from users.models import User
from django import forms
# Register your models here.

# class UserForm(forms.ModelForm):
#   class Meta:
#     model = User
#     fields = '__all__'

admin.site.register(User)