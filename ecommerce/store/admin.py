from django.contrib import admin
from.models import User, Profile, Contact, Product, Cart, CartItem

# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)