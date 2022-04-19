
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def showOrders(request):
    return HttpResponse('Chef Orders')