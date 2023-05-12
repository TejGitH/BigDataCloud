from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Restaurant(models.Model):
    Status = (
        ('A', 'Activate'),
        ('D', 'Deactivate'),
    )
    
    RESTAURANT_NAME = models.CharField(max_length=100)
    RESTAURANT_LOCATION = models.CharField(max_length=100)
    RATING = models.IntegerField()
    CUISINE_TYPE = models.CharField(max_length=100)
    RESTAURANT_IMAGE = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    RESTAURANT_STATUS = models.CharField(max_length=20, choices=Status)

    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    """

    def __str__(self):
        return self.RESTAURANT_NAME + ' - ' + self.RESTAURANT_LOCATION
    
   
    def get_absolute_url(self):
        return reverse("restaurant-detail", kwargs={"pk": self.pk})
    