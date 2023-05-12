from django.urls import path
from incentives.views import (
    IncentiveListView,
    IncentiveDetailView
)

urlpatterns = [
    path('incentive/', IncentiveListView.as_view(), name='incentive-list'),
    path('incentive/<int:pk>/', IncentiveDetailView.as_view(), name='incentive-detail'),  
]