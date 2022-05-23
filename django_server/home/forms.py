from dataclasses import field
from django import forms
from .models import *


class NewShopForm(forms.ModelForm):
    #form for a particular user

    class Meta:
        model = Shop
        fields = ['location','shop_name','shop_description' ,'img']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'input--style-6'}),
            'shop_name': forms.TextInput(attrs={'class': 'input--style-6'}),
            'shop_description': forms.TextInput(attrs={'class': 'textarea--style-6'}),
        }
class NewItemForm(forms.ModelForm):
    #form for a particular user
    class Meta:
        model = FoodItem
        fields = ['name', 'price', 'image', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input--style-6'}),
            'price': forms.TextInput(attrs={'class': 'input--style-6'}),
            'category': forms.TextInput(attrs={'class': 'input--style-6'}),
        }