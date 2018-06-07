from django import forms
from .models import Item, Shopping_list

class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ('title', 'item_type', 'where', 'expires_date', 'on_shopping_list')

class ShoppinglistForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('title', 'on_shopping_list')