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
    path('logout', views.logout),
    path('addnewshop',views.addnewshop),
    path('adminshop',views.adminshop),
    path('updateshop.html', views.updateshop),
]