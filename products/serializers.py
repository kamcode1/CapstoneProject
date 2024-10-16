from rest_framework import serializers
from .models import Product, Cart, CartItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'cart']  # Ensure the relevant fields are included
        extra_kwargs = {'cart': {'read_only': True}}  # Cart will be automatically set in the view

    def validate(self, data):
        product = data.get('product')
        quantity = data.get('quantity')
        
        # Validate stock availability
        if product.stock_quantity < quantity:
            raise serializers.ValidationError(f"Only {product.stock} items left in stock.")
        
        return data
    
class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, source='cartitem_set')
    class Meta:
        model = Cart
        fields = '__all__'
