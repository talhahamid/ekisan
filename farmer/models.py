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


@receiver(post_save, sender=Bit)
def send_acceptance_notification(sender, instance, **kwargs):
    if instance.status:
        message = f'Your bit for {instance.product} is accepted by the {instance.farmer} .'
        Message.objects.create(user=instance.bitter, product=instance.product, notification=message)

       