from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def showOrders(request):
    return HttpResponse('Show Orders')


def paymentStats(request):
    return HttpResponse('Payment Stats')

def editMenu(request):
    return HttpResponse('Edit Menu')

def manageEmployees(request):
    return HttpResponse('Manage Employees')
    
def manageOutlets(request):
    return HttpResponse('Manage Outlets')