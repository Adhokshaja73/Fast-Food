from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse('User Home')

def showCart(request):
    return HttpResponse('Cart')

def showOrders(request):
    return HttpResponse('Orders')

def profilePage(request):
    return HttpResponse('User Profile')
