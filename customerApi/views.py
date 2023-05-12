from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from customerApi.models import Customer
from customerApi.serializer import CustomerSerializer
from rest_framework import generics

class CustomerListView(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
     
    def get(self, request, *args, **kwargs):
        customer = self.get_queryset()
        return render(request, 'customerapi/index.html', {'customer': customer})

class CustomerDetailView(LoginRequiredMixin, generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
