from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    phone_number=models.CharField(max_length=15, unique=True)
    otp=models.CharField(max_length=100,null=True,blank=True)
    is_login=models.BooleanField(default=False)