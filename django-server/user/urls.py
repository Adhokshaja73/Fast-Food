from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('/cart', views.showCart, name="cart"),
    path('/orders', views.showOrders, name="Orders Page"),
    path('/profile', views.profilePage, name="Profile Page"),

]