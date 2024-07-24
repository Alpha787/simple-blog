from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.views import login_user
# from . import views

urlpatterns = [
    path('login_user', login_user, name='login')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
