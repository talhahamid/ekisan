from django.db import models

# Create your models here.

class User(models.Model):
    # Basic information
    name = models.CharField(max_length=255)
    address = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    mobile = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    ROLE_CHOICES = (
        ('farmer', 'Farmer'),
        ('dealer', 'Dealer'),
        ('delivery man', 'Delivery Man')
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    def __str__(self):
        return self.name

class Profilepic(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profilepic=models.CharField(max_length=100)

class Subscription(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    planname=models.CharField(max_length=100)
    expiry_date=models.DateField()
    date=models.DateField()
    amount=models.CharField(max_length=100)
    razor_pay_order_id = models.CharField(max_length=100,null=True,blank=True)  
    razor_pay_payment_id = models.CharField(max_length=100,null=True,blank=True) 
    razor_pay_payment_signature = models.CharField(max_length=100,null=True,blank=True)       
    paid=models.BooleanField(default=False)


