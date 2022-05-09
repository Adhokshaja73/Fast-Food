from distutils.log import Log
import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from hashlib import sha256
from .models import *
# Create your views here.

def landingPage(request):
    if('user' in request.session):
        return(redirect("userdash.html"))
    return(render(request, "index.html"))


def registrationPage(request):
    if('user' in request.session):
        return(redirect("userdash.html"))
    return(render(request, "register.html"))

def register(request):
    if('user' in request.session):
        return(redirect("userdash.html"))
    result = "fail"
    if(request.method == "POST"):
        name = request.POST["name"]
        phone = request.POST["number"]
        email = request.POST["email"]
        uName = request.POST["userName"]
        password = sha256(request.POST["password"].encode('utf-8')).hexdigest()
        role = 1
        newUser = User(user_name = name, user_id = uName, email = email, phone = phone, user_role = role)
        newUser.save()
        newLogin = Login.objects.create(user = newUser, password_hash = password)
        return(render(request, "login.html"))
    return(HttpResponse(result))

def loginPage(request):
    if('user' in request.session):
        return(redirect("userdash.html"))
    return(render(request, "login.html"))

def login(request):
    if('user' in request.session):
        return(redirect("userdash.html"))
    loginStatus = "fail"
    if(request.method == "POST"):
        userName = request.POST["userName"]
        password = sha256(request.POST["password"].encode('utf-8')).hexdigest()
        if(User.objects.filter(user_id = userName).exists()):
            mUser = User.objects.filter(user_id = userName).get()
            if(Login.objects.filter(password_hash = password).exists()):
                request.session['user'] = mUser.user_id
                return(redirect("userdash.html"))
            else:
                loginStatus = "Wrong password"
        else:
            loginStatus = "User does not existS"
    return(HttpResponse(loginStatus))

def logout(request):
    if('user' not in request.session):
        return(redirect("index.html"))
    del request.session['user']
    del request.session['cart']
    return(redirect('login.html'))

def userDash(request):
    if('user' not in request.session):
        return(render(request, 'index.html'))
    foodItems = FoodItem.objects.all()
    return(render(request, "userdash.html", { 'foodItems' : foodItems }))

def addToCart(request):
    if(request.method == "POST"):
        newItm = request.POST['item']
        if('cart' not in request.session):
            request.session['cart'] = []
        if(newItm not in request.session['cart']):
            request.session['cart'].append(newItm)  
        print(request.session['cart'])        
  
        return(redirect("userdash.html"))
    else:
        print("Something wrong")
        return(redirect("userdash.html"))

def showCart(request):
    if('user' not in request.session):
        return(redirect("userdash.html"))
    items = request.COOKIES.get('sessionid')
    print(items)
    return(render(request, 'cart.html', { 'foodItem' : items}))

def placeOrderPage(request):
    if('user' not in request.session):
        return(redirect("userdash.html"))
    else:
        return(render(request, 'placeorder.html'))

def vendorRegistrationPage(requst):
    return(HttpResponse("Vendor registration"))



