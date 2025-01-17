from rest_framework import serializers
from .models import UserCart
from shop.models import Product

class AddToCartSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1, default=1)

    class Meta:
        model = UserCart
        fields = ['product_id', 'quantity']

    def validate_product_id(self, value):
        try:
            Product.objects.get(id=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product not found")
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        product = Product.objects.get(id=validated_data['product_id'])
        
        # Check if product already exists in cart
        cart_item, created = UserCart.objects.get_or_create(
            user=user,
            product=product,
            defaults={'quantity': validated_data['quantity']}
        )
        
        if not created:
            # Update quantity if product already in cart
            cart_item.quantity += validated_data['quantity']
            cart_item.save()
            
        return cart_item