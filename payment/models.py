from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile

class Payment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    amount = models.CharField(max_length=10)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
