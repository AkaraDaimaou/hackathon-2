from django.urls import path
from .views import ProductListCreateView, ProductDetailView, CartListCreateView, CartDetailView, ContactCreateView, register, login, home

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('contact/', ContactCreateView.as_view(), name='contact-create'),
    path('auth/register/', register, name='register'),
    path('auth/login/', login, name='login'),
    path('', home, name='home'),
]


