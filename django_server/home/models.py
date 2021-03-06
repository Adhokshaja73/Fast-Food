import imp
from operator import mod
from pyexpat import model
from django.db import models
from . import *
from .constats import *
# Create your models here.


class User(models.Model):
    USER_ROLES =  (
        (0,  "Student"),
        (1, "ShopAdmin"),
    )
    user_id = models.CharField( max_length =256, primary_key=True) 
    user_name = models.CharField( max_length =50) 
    email = models.CharField( max_length =100) 
    phone = models.CharField( max_length =10)
    user_role = models.IntegerField(choices= USER_ROLES) 
    def __str__(self):
        return (self.user_id)


class Login(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True) 
    password_hash = models.CharField( max_length =64) 
    def __str__(self):
        return (self.user.user_id)



class Shop(models.Model):
    shop_id = models.CharField( max_length =256, primary_key=True) 
    location = models.CharField( max_length =10) 
    shop_name = models.CharField (max_length = 20) 
    shop_description = models.CharField( max_length =100)
    img = models.ImageField(upload_to = "images/shops/")
    def __str__(self):
        return (self.shop_name)

class Owns(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE) 
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE) 


class Order(models.Model):
    ORDER_STATUS = (
        (0, "New"),
        (1, "Processing"),
        (2, "ReadyToServe"),
        (3, "Complete"),
        (-1, "Cancelled")
    )
    order_id = models.CharField( max_length =256, primary_key=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    order_status = models.IntegerField(choices = ORDER_STATUS) 
    notes = models.CharField( max_length =100)
    order_date_time = models.DateTimeField()
    delivery_date_time = models.DateTimeField()
    def __str__(self):
        return (self.order_id)


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(("Amount"), null=False, blank=False)
    
    status = models.CharField(
        ("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        ("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        ("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        ("Signature ID"), max_length=128, null=False, blank=False
    )

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}" 


class FoodItem(models.Model):
    AVAILABILITY_STATUS = (
        (0, "Available"),
        (1, "Unavailable"),
    )
    item_id = models.CharField( max_length =256, primary_key=True) 
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE) 
    price = models.DecimalField(max_digits = 5, decimal_places=2) 
    name = models.CharField( max_length =50) 
    status = models.IntegerField(choices=AVAILABILITY_STATUS) 
    image = models.FileField(upload_to="images/fooditems/")
    category = models.CharField( max_length =50)    
  


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE) 
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE) 
    item_count = models.IntegerField() 
  


class OffDays(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE) 
    date  = models.DateField()
    start= models.TimeField()
    end = models.TimeField()