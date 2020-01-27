from django import forms
from .models import Order

class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2017, 2036)]

    credit_card_number = forms.CharField(label="Credit card number", min_length=12, required=False)
    cvv = forms.CharField(label="Security code (CVV)", max_length=3, required=False)
    expiry_month = forms.ChoiceField(label="Month", choices = MONTH_CHOICES, required= False)
    expiry_year = forms.ChoiceField(label="Year", choices = YEAR_CHOICES, required= False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
    full_name = forms.CharField(error_messages={'required':'Full name is required'})
    country = forms.CharField(error_messages={'required':'Please insert country'})
    town_or_city = forms.CharField(error_messages={'required':'Please insert town or a city'})
    street_address1 = forms.CharField(error_messages={'required':'Please insert street address'})
    class Meta:
        model = Order
        fields = (
            "full_name", "phone_number", "country", 
            "post_code", "town_or_city", "street_address1",
            "street_address2", "county")
