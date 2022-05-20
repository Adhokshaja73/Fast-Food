from django import forms
from .models import *


class NewShopForm(forms.ModelForm):
    #form for a particular user
    class Meta:
        model = Shop
        fields = ['location', 'shop_name', 'shop_description', 'img']

class NewItemForm(forms.ModelForm):
    #form for a particular user
    class Meta:
        model = FoodItem
        fields = ['name', 'price', 'image', 'category']