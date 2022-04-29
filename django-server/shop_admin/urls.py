from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.orders),
    path('payments', views.payments),
    path('edit_menu', views.edit_menu),
    path('manage_employees', views.manage_employees),
    path('add_new_shop', views.manage_outlets)
]
