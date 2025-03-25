from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    call_sign = models.CharField(max_length=10, blank=True, null=True)
    membership_expires = models.DateField()
    is_active = models.BooleanField(default=False)
    dues_paid = models.BooleanField(default=False)  # New field

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
