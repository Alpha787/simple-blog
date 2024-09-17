from django.urls import path
from .views import PostView, PostDetailView, PostDeleteView, HomeView, see_request, user_info, private_place, staff_place, add_messages
# from django.views.generic import TemplateView


urlpatterns = [
    # path('', post_list, name='post_list'),
    path('', HomeView.as_view(), name="homepage"),
    path('post/<post_id>', PostDetailView.as_view()),
    path('post/<post_id>/delete', PostDeleteView.as_view()),
    path('see_request/', see_request),
    path('user_info/', user_info),
    path('private_place/', private_place),
    path('staff_place/', staff_place),
    path('add_message/', add_messages),
]
