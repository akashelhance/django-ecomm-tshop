from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def home(request):
    return render(request, template_name='store/home.html')

def cart(request):
    return render(request, template_name='store/cart.html')

def login(request):
    return render(request, template_name='store/login.html')

def signup(request):
    return render(request, template_name='store/signup.html')

def orders(request):
    return render(request, template_name='store/orders.html')