from django.urls import path, include
from . import views


#creation of project urls

urlpatterns = [
path("accounts/", include("django.contrib.auth.urls")),
path('createProject', views.create_project, name='createProject'),
path('list', views.project_list, name='project-list'),
path('edit/<int:pk>/', views.edit_profile, name='profile-edit'),
path('register/', views.register, name="register"),
path('', views.view_profile, name='profile'),
path('upload/', views.upload, name='upload'),

]


