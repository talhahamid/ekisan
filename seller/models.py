from django.db import models
from accounts.models import User

# Create your models here.
class Products(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    productname = models.CharField(max_length=255)
    producttype = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    img1= models.CharField(max_length=255)
    img2=models.CharField(max_length=255)
    img3=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)