from django.urls import path
from .views import UserCreateView, ProfileView, ContactCreateView, ProductListView, CartView, AddToCartView, RemmoveFromCartView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductListView.as_view(), name='product-detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/', RemmoveFromCartView.as_view(), name='remove-from-cart'),
]
