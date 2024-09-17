from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.views import login_user, register, login_view
# from . import views

urlpatterns = [
    # path('login_user', login_user, name='login'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
