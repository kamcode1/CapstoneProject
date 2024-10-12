from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    SELLER = 'seller'
    BUYER = 'buyer'
    ROLE_CHOICES = [
        (SELLER, 'seller'),
        (BUYER, 'Buyer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default = BUYER)

    def __str__(self) -> str:
        return self.username