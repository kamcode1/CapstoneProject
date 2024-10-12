from django.core.exceptions import ValidationError
from django.db import models
from users.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    stock_quantity = models.IntegerField()
    image_url = models.URLField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'seller'})

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    buyer = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': 'buyer'})
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.buyer.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):

        if self.product.stock_quantity < self.quantity:
            raise ValidationError("Not enough stock available")
        self.product.stock_quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in cart"
    
    
                                                                                  