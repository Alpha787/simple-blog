from django.urls import path
from .views import PostView, PostDetailView, PostDeleteView, HomeView
# from django.views.generic import TemplateView


urlpatterns = [
    # path('', post_list, name='post_list'),
    path('', HomeView.as_view(), name="homepage"),
    path('post/<post_id>', PostDetailView.as_view()),
    path('post/<post_id>/delete', PostDeleteView.as_view()),
]
