# serializers.py

from rest_framework import serializers
from customers .models import Customer, Address, OrderItem,Product,Order
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 6}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'address_line1', 'address_line2', 'city', 'state', 'country', 'postal_code')

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    addresses = AddressSerializer(many=True, required=False)

    class Meta:
        model = Customer
        fields = ('user', 'phone_number', 'addresses')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = User.objects.create_user(**user_data, password=password)
        
        addresses_data = validated_data.pop('addresses', [])
        customer = Customer.objects.create(user=user, **validated_data)
        
        for address_data in addresses_data:
            Address.objects.create(customer=customer, **address_data)
        
        return customer
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('product_name', 'quantity', 'price')

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'address', 'total_amount', 'created_at', 'updated_at', 'status', 'order_items')
