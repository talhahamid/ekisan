from django.db import models
from accounts.models import User

# Create your models here .

class DeliverynmanProfilePic(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profilepic=models.CharField(max_length=100)
