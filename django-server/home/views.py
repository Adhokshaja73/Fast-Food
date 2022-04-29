from pydoc_data.topics import topics
import re
from tempfile import tempdir
from tkinter.tix import Select
from django.shortcuts import render
from django.http import HttpResponse
from home.models import *

# Create your views here.
def home(request):  
    topItems = food_item.objects.all()
    
    return(render(request, 'index.html', {'topItems' : topItems}))


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