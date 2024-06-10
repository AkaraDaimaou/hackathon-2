from django.urls import path
from .views import UserCreateView, ProfileView, ContactCreateView, ProductListView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductListView.as_view(), name='product-detail'),
]
