from django import forms
from .models import User
from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)
  confirm_password = forms.CharField(widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('email', 'password', 'confirm_password')

class UserLoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)
  captcha = CaptchaField()
