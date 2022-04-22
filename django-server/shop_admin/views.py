from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def orders(request):
    return render(request, 'admindash.html')

def payments(request):
    return HttpResponse('payments')

def edit_menu(request):
    return HttpResponse('Edit menu')

def manage_employees(request):
    return HttpResponse('Manage Employees')

def manage_outlets(request):
    return render(request , 'addnewshop.html')
