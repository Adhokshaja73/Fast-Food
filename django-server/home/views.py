from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return(HttpResponse('Hello world'))


def login(request):
    return(HttpResponse('Login'))


def register(request):
    return(HttpResponse('register'))