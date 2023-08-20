from django import forms
from .models import Product, Specialoffer, Store

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'expiration_date']
        
class SpecialofferForm(forms.ModelForm):
    class Meta:
        model = Specialoffer
        fields = ['store', 'offer_product']

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name']