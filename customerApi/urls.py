from django.urls import path
from customerApi.views import (
    CustomerListView,
    CustomerDetailView
)

urlpatterns = [
    #path('', views.home, name='home1'),
    path('customer/', CustomerListView.as_view(), name='cust-list'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='cust-detail'),  
]