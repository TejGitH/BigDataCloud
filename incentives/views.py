from django.shortcuts import render
from .serializer import IncentiveSerializer
from .models import Incentive
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics

# Create your views here.

class IncentiveListView(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Incentive.objects.all()
    serializer_class = IncentiveSerializer

    def get(self, request, *args, **kwargs):
        incentive = self.get_queryset()
        return render(request, 'incentives/incentive_index.html', {'incentive': incentive})
   
#to be corrected

class IncentiveDetailView(LoginRequiredMixin, generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Incentive.objects.all()
    serializer_class = IncentiveSerializer
