from django.contrib.auth.models import User 
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartProduct')

    def __str__(self):
        return f'Cart of {self.user.username}'

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product.name} in cart of {self.cart.user.username}'

User = get_user_model()

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    message = models.TextField()

    def __str__(self):
        return self.message
