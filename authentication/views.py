from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from authentication.serializer import RestaurantSerializer
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Restaurant

def home(request):
    return render(request, 'authentication/home.html')
class RestaurantListView(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = RestaurantSerializer
    template_name = 'authentication/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'restaurants'
    #ordering = ['-date_posted'] 

    def get_queryset(self):
        return Restaurant.objects.all()
class RestaurantCreateView(LoginRequiredMixin, CreateView):
    model = Restaurant
    fields = ['RESTAURANT_NAME', 'RESTAURANT_LOCATION', 'RATING', 'CUISINE_TYPE', 'RESTAURANT_STATUS']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class RestaurantDetailView(DetailView):
    model = Restaurant
    
class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    fields = ['RESTAURANT_NAME', 'RESTAURANT_LOCATION', 'RATING', 'CUISINE_TYPE', 'RESTAURANT_STATUS']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class RestaurantDeleteView(LoginRequiredMixin, DeleteView):
    model = Restaurant
    success_url = '/'
