from django.urls import path, include
from . import views


# #creation of project urls

urlpatterns = [

path('create_hood', views.NeighbourhoodCreateView.as_view(), name='hood-create'),
path('list_hood', views.NeighbourhoodListView.as_view(), name='hood-list'),
path('hood/<int:pk>/', views.NeighbourhoodDetailView.as_view(), name='hood-detail'),
path('hood/<int:pk>/update', views.NeighbourhoodUpdateView.as_view(), name='hood-update'),
path('hood/<int:pk>/delete/', views.NeighbourhoodDeleteView.as_view(), name='hood-delete'),

path('create_business', views.BusinessCreateView.as_view(), name='business-create'),
path('list_business', views.BusinessListView.as_view(), name='business-list'),
path('business/<int:pk>/', views.BusinessDetailView.as_view(), name='business-detail'),



]


