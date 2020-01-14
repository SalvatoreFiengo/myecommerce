from django import forms
from products.models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "category", "image","price", "offer", "description", "stock")
