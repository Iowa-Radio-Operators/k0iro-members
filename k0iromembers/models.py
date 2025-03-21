from django.db import models

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    date_entered = models.DateField(auto_now_add=True)  # Automatically set when created
    date_membership_over = models.DateField()
    call_sign = models.CharField(max_length=50, blank=True, null=True)  # Add Call Sign
    paid_in_full = models.BooleanField(default=False)  # Add Paid in Full