from django.urls import path
from .views import PostView, PostDetailView, PostDeleteView
# from django.views.generic import TemplateView


urlpatterns = [
    # path('', post_list, name='post_list'),
    path('', PostView.as_view()),
    path('post/<post_id>', PostDetailView.as_view()),
    path('post/<post_id>/delete', PostDeleteView.as_view()),
]
