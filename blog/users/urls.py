from django.urls import path, include
from users.views import users_list

urlpatterns = [
    path('user', users_list, name='users_data')
]
