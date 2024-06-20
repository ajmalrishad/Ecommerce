from django import forms
from .models import Product,Customer, Rating

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'