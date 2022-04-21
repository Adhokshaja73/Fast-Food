import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return(HttpResponse('Hello world'))


def login(request):
    return(render(request, 'login.html'))


def register(request):
    return(render(request, 'register.html'))

def validateUser(request):
    print(request.POST)
    userId = request.POST['mUser']
    password = request.POST['mPass']
    if(userId == "abcd" and password == "1234"):
        return(render(request, 'new.html'))
    else:
        return(render(request, 'login.html', {'error' : 'Invalid UserName'}))