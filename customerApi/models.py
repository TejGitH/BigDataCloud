from django.db import models
from django.urls import reverse


class Customer(models.Model):
    username=models.CharField(max_length=200, unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=200)
    tel=models.PositiveIntegerField()
    DOB=models.DateField()
    tablebook=models.PositiveIntegerField()
    orders=models.CharField(max_length=200)
    orders_count=models.PositiveIntegerField(default=0)
    feedback=models.CharField(max_length=200)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + ' - ' + self.last_name
    
    def get_absolute_url(self):
        return reverse("cust-detail", kwargs={"pk": self.pk})
    
    def add_points(self, points):
        self.points += points
        self.save()
    