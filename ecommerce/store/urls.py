from django.urls import path
from .views import UserCreate, ProfileView, ContactCreateView, ProductListView, CartView, AddToCartView, RemoveFromCartView

urlpatterns = [
    path('users/', UserCreate.as_view(), name='user-create'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    #path('cart/page/', cart_page, name='cart-page'),
]
