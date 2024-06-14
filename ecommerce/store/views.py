from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Product, Cart, Contact
from django.contrib.auth import login as auth_login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

# Home View
def home(request):
    return render(request, 'home.html')

# Product Views
class ProductListCreateView(ListView, CreateView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    fields = ['name', 'price', 'description', 'image']

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

# Cart Views
class CartListCreateView(ListView, CreateView):
    model = Cart
    template_name = 'cart_page.html'
    context_object_name = 'cart_items'
    fields = ['product', 'quantity']

class CartDetailView(DetailView):
    model = Cart
    template_name = 'cart_detail.html'
    context_object_name = 'cart_item'

# Contact View
class ContactCreateView(CreateView):
    model = Contact
    template_name = 'contact.html'
    fields = ['name', 'email', 'message']
    success_url = '/'  # Redirect after successful form submission

# Authentication Views
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to home page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('/')
    return render(request, 'login.html')
