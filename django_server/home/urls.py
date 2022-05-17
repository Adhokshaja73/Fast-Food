from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landingPage),
    path('login.html', views.loginPage),
    path('login', views.login),
    path('register.html', views.registrationPage),
    path('register', views.register),
    path('userdash.html', views.userDash),
    path('addToCart', views.addToCart),
    path('cart.html', views.showCart),
    path('profile.html', views.profile),
    path('placeorder.html', views.placeOrderPage),
    path('placeOrder', views.placeOrder ),
    path('logout', views.logout),
    path('addnewshop.html',views.addnewshop),
    path('saveNewShop',views.saveNewShop),
    path('adminshop.html',views.adminshop),
    path('updateshop.html', views.updateshop),
    path('showdetail',views.showdetail),
    path('shop_profile',views.shop_profile),
    path('payment.html',views.paymentPage),
    path('make_payment',views.makePayment),
    path('my_order',views.my_order),
    path('payment',views.payment),
    path('additem.html',views.additem),
    path('updateitem',views.updateitem)

]