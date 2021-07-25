from django.urls import path, include
from . import views


# #creation of project urls

urlpatterns = [

path('create_neighbourhood', views.NeighbourhoodCreateView.as_view(), name='create_neighbourhood'),
path('list_neighbourhood', views.NeighbourhoodListView.as_view(), name='list_neighbourhood'),
path('detail_neighbourhood/<int:pk>/', views.NeighbourhoodDetailView.as_view(), name='detail_neighbourhood'),


]


