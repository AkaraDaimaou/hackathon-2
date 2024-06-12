from django.urls import path
from .views import UserCreate, ProfileView, ContactCreateView, ProductListView, CartView, AddToCartView, RemoveFromCartView, login_view, signup_view, logout_view

urlpatterns = [
    path('users/', UserCreate.as_view(), name='user-create'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    #path('cart/page/', cart, name='cart-page'),
]
