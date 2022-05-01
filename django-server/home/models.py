import email
from statistics import mode
from django.db import models

# Create your models here.

 

class  user(models.Model):
    user_id = models.CharField( max_length =10, primary_key=True) 
    user_name = models.CharField( max_length =50) 
    email = models.CharField( max_length =100) 
    phone = models.CharField( max_length =10)
    user_role = models.DecimalField( max_digits =1, decimal_places = 0) 
    def __str__(self):
        return (self.name)


class login(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE) 
    password_hash = models.CharField( max_length =64) 
    def __str__(self):
        return (self.name)

class owns(models.Model):
    admin_id = models.CharField( max_length =10) 
    shop_id = models.CharField( max_length =10) 
    def __str__(self):
        return (self.name)

class shop(models.Model):
    shop_id = models.CharField( max_length =10, primary_key=True) 
    location = models.CharField( max_length =10) 
    name = models.CharField (max_length = 20) 
    shop_description = models.CharField( max_length =100)
    def __str__(self):
        return (self.name)


class order(models.Model):
    order_id = models.CharField( max_length =10, primary_key=True) 
    user = models.ForeignKey(user, on_delete=models.CASCADE) 
    shop = models.ForeignKey(shop, on_delete=models.CASCADE)
    order_status = models.DecimalField( max_digits =1, decimal_places = 0) 
    notes = models.CharField( max_length =100)
    order_date = models.DateField 
    order_= models.TimeField 
    delivery_date = models.DateField 
    delivery_= models.TimeField 
    def __str__(self):
        return (self.name)

class chef_orders(models.Model):
    chef = models.ForeignKey(user, on_delete=models.CASCADE ) 
    oder = models.ForeignKey(order, on_delete=models.CASCADE) 
    def __str__(self):
        return (self.name)



class works_for(models.Model):
    chef = models.ForeignKey(user, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(shop, on_delete=models.CASCADE)
    def __str__(self):
        return (self.name)



class payments(models.Model):
    payment_id = models.CharField( max_length =10, primary_key=True) 
    user = models.ForeignKey(user, on_delete=models.CASCADE) 
    shop = models.ForeignKey(shop , on_delete=models.CASCADE) 
    amount = models.DecimalField( max_digits =4, decimal_places=3) 
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    status = models.DecimalField( max_digits =1, decimal_places = 0) 
    def __str__(self):
        return (self.name)


class food_item(models.Model):
    item_id = models.CharField( max_length =10, primary_key=True) 
    shop = models.ForeignKey(shop, on_delete=models.CASCADE) 
    price = models.FloatField(4) 
    name = models.CharField( max_length =50) 
    status = models.DecimalField( max_digits =1, decimal_places = 0) 
    image_url = models.CharField( max_length =500) 
    category = models.CharField( max_length =50)    
    def __str__(self):
        return (self.name)


class order_items(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE) 
    food_item = models.ForeignKey(food_item, on_delete=models.CASCADE) 
    item_count = models.DecimalField( max_digits =2 , decimal_places = 0) 
    def __str__(self):
        return (self.name)


class off_days(models.Model):
    shop = models.ForeignKey(shop, on_delete=models.CASCADE) 
    date  = models.DateField()
    start_= models.TimeField 
    end_= models.TimeField  
    def __str__(self):
        return (self.name)