from django.contrib import admin
from.models import Product, Cart, CartProduct, Contact

# Register your models here.

class CartProductInline(admin.TabularInline):
    model = CartProduct

class CartAdmin(admin.ModelAdmin):
    inlines = [CartProductInline]

admin.site.register(Product)
admin.site.register(Cart, CartAdmin)
admin.site.register(Contact)

