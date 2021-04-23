from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms.authforms import CustomerCreationForm, CustomerAuthForm
from django.contrib.auth import authenticate, login as LoginDjango, logout
from store.models import Tshirt

# Create your views here.

def showproduct(request, id):
    tshirt =Tshirt.objects.get(id=id)
    context ={
        "tshirt": tshirt
    }
    return render(request, template_name='store/product_details.html',  context= context)
    
     

def home(request):
    print(request.user)
    tshirts = Tshirt.objects.all()
    print(len(tshirts)) 

    
    context ={
        "tshirts": tshirts
    }
    return render(request, template_name='store/home.html',  context= context)

def cart(request):
    return render(request, template_name='store/cart.html')

def login(request):
    if request.method == 'POST':
        form=CustomerAuthForm(data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user:
                LoginDjango(request, user)
                return redirect('homepage')
            else:
                pass

        else:
            context ={
            "form":form
        }
        return render(request, template_name='store/login.html' , context=context)

        
    else:
        form= CustomerAuthForm()
        context ={
            "form":form
        }
        return render(request, template_name='store/login.html' , context=context)

def signup(request):
    if request.method=='POST':
        form=CustomerCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.email=user.username
            user.save()
            print(user)
            return render(request, template_name='store/login.html')
        else:
            context ={
            "form":form
        }
            return render(request, template_name='store/signup.html', context=context)

    else:
        form=CustomerCreationForm()
        context ={
            "form":form
        }
        return render(request, template_name='store/signup.html', context=context)

def orders(request):
    return render(request, template_name='store/orders.html')

def signout(request):
    # request.session.clear()
    logout(request)
    return render(request, template_name='store/home.html')