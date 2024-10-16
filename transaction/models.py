from django.db import models
from users.models import User

class Transaction(models.Model):
    PENDING = 'pending'
    SUCCESS = 'success'
    FAILED = 'failed'

    STATUS_CHOICES = [
        (PENDING, 'pending'),
        (SUCCESS, 'Success'),
        (FAILED, 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transaction {self.reference} by {self.user.username}" 