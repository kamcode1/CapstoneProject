# products/views.py

from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated
from .models import Product, Cart, CartItem
from .serializers import ProductSerializer, CartSerializer, CartItemSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

class CartItemViewSet(viewsets.ModelViewSet):  # Added the missing CartItemViewSet
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cart = Cart.objects.get_or_create(buyer=self.request.user)
        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']

        if product.stock_quantity >= quantity:
            product.stock_quantity -= quantity
            product.save()

            serializer.save(cart=cart)
        else:
            raise serializers.ValidationError("Not enough stock available for the product.")

    def get_queryset(self):
        """
        Override the default queryset to return only items in the user's cart.
        """
        cart = Cart.objects.get(buyer=self.request.user)
        return CartItem.objects.filter(cart=cart)