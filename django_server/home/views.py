from distutils.log import Log
import re
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render, redirect
from hashlib import sha256
from .models import *
import random
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
    try:
        items = request.COOKIES.get('cart')
        items = set(items[1:-1].replace("\"",'').split(","))
        print(items)
        foodItems = []
        print(request.COOKIES.get('cart'))
        for i in items:
            foodItems.append(FoodItem.objects.filter(item_id = i ).get())
        print(foodItems)
        response = render(request, 'cart.html', { 'foodItem' : foodItems}) 
        return(response)
    except Exception as e:
        print(e)
        return(render(request, 'cart.html', { 'msg' : "Cart is empty"}))
    

    

def placeOrderPage(request):
    if('user' not in request.session):
        return(redirect("userdash.html"))
    else:
        return(render(request, 'placeorder.html'))

def vendorRegistrationPage(requst):
    return(HttpResponse("Vendor registration"))

def addnewshop(request):
    return(render(request, 'addnewshop.html'))
        #shop_id=random.randrange(100, 200, 1)
        #shop_name = request.POST["outlet_name"]
        #location = request.POST["location"]
        #desc=request.POST["description"]
        #newshop = Shop(shop_id=1,shop_name = name,location=location,description=desc)
        #newshop.save()
        #return(render(request, "shopadmindash.html"))

#def addnewShop(request):
 #    if(request.method == "POST"):
  #      return(render(request, 'userdash.html'))
    #return(render(request, 'addnewshop.html'))
    #if(request.method == "POST"):
   
        #shop_id=random.randrange(100, 200, 1)
        #shop_name = request.POST["outlet_name"]
        #location = request.POST["location"]
        #desc=request.POST["description"]
        #newshop = Shop(shop_id=1,shop_name = name,location=location,description=desc)
        #newshop.save()
        #return(render(request, "shopadmindash.html"))


def adminshop(request):
    foodItems = Shop.objects.all()
    return(render(request, "shopadmindash.html", { 'foodItems' : foodItems }))

def profile(request):
    return(render(request, 'profile.html'))

def updateshop(request):
    return(render(request, 'updateshop.html'))

def showdetail(request):
    return(render(request,'showdetail.html'))

def shop_profile(request):
    return(render(request, 'shop_profile.html'))

def my_order(request):
    return(render(request,'myorder.html'))

def payment(request):
    return(render(request, 'payment.html'))



