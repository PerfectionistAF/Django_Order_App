from rest_framework import serializers
from .models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
##1:1 rather than Many:Many , so no need for intermediatry table
class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)
    quantity = serializers.IntegerField(write_only=True)

    class Meta:
        model = Order
        fields = ['status', 'product', 'quantity']

    def validate(self, data):
        product = data['product']
        quantity = data['quantity']
        if not product.is_active:
            raise serializers.ValidationError(f"Inactive product: {product.name}")
        if product.stock < quantity:
            raise serializers.ValidationError(f"Insufficient stock for {product.name}")
        return data

    def create(self, validated_data):
        product = validated_data.pop('product')
        quantity = validated_data.pop('quantity')
        order = Order.objects.create(**validated_data)

        OrderItem.objects.create(order=order, product=product, quantity=quantity)
        product.stock -= quantity
        product.save()

        return order

        
class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']
        
    def validate(self, data):
        product = data['product']
        quantity = data['quantity']

        if not product.is_active:
            raise serializers.ValidationError(f"Inactive product: {product.name}")
        if product.stock < quantity:
            raise serializers.ValidationError(f"Insufficient stock for {product.name}")

        return data
