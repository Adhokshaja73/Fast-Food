from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'userdash.html')

def showCart(request):
    return render(request, 'cart.html')

def showOrders(request):
    return HttpResponse('Orders')

def profilePage(request):
    return render(request, 'profile.html')

def placeorder(request):
    return render(request, 'placeorder.html')
