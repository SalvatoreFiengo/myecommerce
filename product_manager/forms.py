from django import forms
from products.models import Product


class AddProductForm(forms.ModelForm):
    name = forms.CharField(error_messages={'required':'Product name is required'})
    price = forms.CharField(error_messages={'required':'Please insert a price for your product'})
    description = forms.CharField(error_messages={'required':'Please insert a description of your product'})
    class Meta:
        model = Product
        fields = ("name", "category", "image","price", "offer", "description", "stock", "id")

    def clean_price(self):
        """password validation method"""
        price = self.cleaned_data.get('price')
        if price == "0":
            raise forms.ValidationError(u'Please insert a price for your product')
        return price
    def clean_stock(self):
        """password validation method"""
        stock = self.cleaned_data.get('stock')
        if stock == 0:
            raise forms.ValidationError(u'Please insert product quantity')
        return stock