from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Cart, CartProduct, Contact, User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    products = CartProductSerializer(many=True, read_only=True, source='cartproduct_set')

    class Meta:
        model = Cart
        fields = ['id', 'user', 'products']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
