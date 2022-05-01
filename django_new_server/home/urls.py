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
    path('accounts/', include('allauth.urls')),
]