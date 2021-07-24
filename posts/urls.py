from django.urls import path
from .views import PostListView, PostDetailView
from . import views
urlpatterns = [
path('post', PostListView.as_view(), name='post-home'),
path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),


]