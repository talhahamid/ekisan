from django.db import models
from accounts.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
from dealer.models import Bit
from django.utils import timezone


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
    

class Message(models.Model):
    user = models.CharField(max_length=20)
    notification = models.TextField()
    product = models.CharField(max_length=20)

class Tracking(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=100)
    delivery_status = models.CharField(max_length=50, default='Pending')
    delivery_date = models.DateField(null=True, blank=True) 

       

class Agreement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    agree = models.BooleanField(default=False)      


from django.db import models

from django.db import models

class Farm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Store GPS coordinates or use a GeoDjango field for advanced location handling
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    # Optional: Farm description, link to an external video streaming service, etc.
    description = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)


class Renter(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    city=models.CharField(max_length=250)
    img1=models.CharField(max_length=250)
    img2=models.CharField(max_length=250)
    img3=models.CharField(max_length=250)
    duration=models.CharField(max_length=250)
    rent=models.CharField(max_length=250)
    location=models.CharField(max_length=250)