from distutils.log import Log
import re
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.

def landingPage(request):
    return(render(request, "index.html"))

def loginPage(request):
    return(render(request, "login.html"))

def login(request):
    loginStatus = "fail"
    if(request.method == "POST"):
        userName = request.POST["userName"]
        password = hash(request.POST["password"])
        if(User.objects.filter(user_id = userName).exists()):
            mUser = User.objects.filter(user_id = userName).get()
            if(Login.objects.filter(password_hash = password).exists()):
                return(render(request, "index.html"))
            else:
                loginStatus = "Wrong password"
        else:
            loginStatus = "User does not existS"
    return(HttpResponse(loginStatus))

def registrationPage(request):
    return(render(request, "register.html"))

def register(request):
    result = "fail"
    if(request.method == "POST"):
        name = request.POST["name"]
        phone = request.POST["number"]
        email = request.POST["email"]
        uName = request.POST["userName"]
        password = hash(request.POST["password"])
        role = 1
        newUser = User(user_name = name, user_id = uName, email = email, phone = phone, user_role = role)
        newUser.save()
        newLogin = Login.objects.create(user = newUser, password_hash = password)
        return(render(request, "login.html"))
    return(HttpResponse(result))

def vendorRegistrationPage(requst):
    return(HttpResponse("Vendor registration"))




