from django.urls import path
from . import views
from .views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
    RestaurantUpdateView,
    RestaurantDeleteView,
)

urlpatterns = [
    path('', views.home, name='home1'),
    path('restaurant/', RestaurantListView.as_view(), name='home'),
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),    
    path('restaurant/new/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('restaurant/<int:pk>/update/', RestaurantUpdateView.as_view(), name='restaurant-update'),    
    path('restaurant/<int:pk>/delete/', RestaurantDeleteView.as_view(), name='restaurant-delete'),
]