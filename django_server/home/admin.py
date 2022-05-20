from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Login)
admin.site.register(FoodItem)
admin.site.register(Shop)
admin.site.register(Payments)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Owns)


