
from cgi import print_form
from datetime import date, datetime
from time import time
from tkinter import NS
from tkinter.messagebox import NO
from unittest import addModuleCleanup
from urllib import request, response
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
        role = request.POST["role"]
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
    return(redirect('login.html'))

def userDash(request):
    if('user' not in request.session):
        return(render(request, 'index.html'))
    else:
        currentUser = User.objects.filter(user_id = request.session['user']).get()
        if(currentUser.user_role == 0 ):
            foodItems = FoodItem.objects.all()
            return(render(request, "userdash.html", { 'foodItems' : foodItems }))
        else:
            return(redirect("adminshop.html"))

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

def placeOrder(request):
    if('user' not in request.session):
        redirect("index.html")
    elif( request.method != "POST"):
        print("Not post")
        redirect("placeorder.html")
    else:
        cartMap = request.COOKIES.get("cartMap").replace("\"",'')[1:-1]
        cartMap = str(cartMap.split(",")).replace('\'','').replace(" ",'')[1:-1].split(",");  
        print(cartMap)
        items = {}
        for i in cartMap:
            print(i)
            curr = i[1:-1].split(":")
            items[curr[0]] = int(curr[1])
        print(items)


        nOrderId = sha256((request.session['user'] + str(datetime.now())).encode('utf-8')).hexdigest()
        nUser = User.objects.filter(user_id = request.session['user']).get()
        nShop = Shop.objects.filter(shop_id = request.COOKIES.get('selectedShop')).get()
        nOrder_status = 0
        nNotes = request.POST['notes']
        nOrder_date_time = datetime.now()
        nDelivery_date_time = request.POST['date']+" "+request.POST['time']

    
        billAmt = 0

        newOrder = Order(order_id = nOrderId, user = nUser, shop = nShop, order_status = nOrder_status, notes = nNotes, order_date_time = nOrder_date_time, delivery_date_time = nDelivery_date_time)
        newOrder.save()
        for i in items:
            orderItem = OrderItem(order = newOrder, food_item = FoodItem.objects.filter(item_id = i).get(), item_count = items[i])
            orderItem.save()
            billAmt += FoodItem.objects.filter(item_id = i).get().price * items[i]
        print("\n\n\n\n\n\n",billAmt)
        nPayId = sha256(nOrderId.encode('utf-8')).hexdigest()
        nPayment = Payments(payment_id = nPayId, user = nUser, shop = nShop, amount = billAmt, order = newOrder, status = 0)
        nPayment.save()
        return(redirect("payment.html"))


def paymentPage(request):
    return(render(request, "payment.html"))
def makePayment(request):
    return(redirect("userdash.html"))

def vendorRegistrationPage(requst):
    return(HttpResponse("Vendor registration"))

def addnewshop(request):
    return(render(request, 'addnewshop.html'))

def saveNewShop(requet):
    if(requet.method != 'POST'):
        return(redirect("userdash.html"))
    elif('user' in request.session):
        currentUser = User.objects.filter(user_id = request.session['user']).get()
        if(currentUser.user_role == 1 ):
            pass
        else:
            return(redirect(""))
    else:
        return(redirect(""))

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



