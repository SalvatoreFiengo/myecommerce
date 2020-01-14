from django import forms
from django.forms import SelectDateWidget, DateField, BooleanField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile
from helper.functions import previous_years


class UserLoginForm(forms.Form):
    """Form to be used to log users in"""

    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""

    password1 = forms.CharField(label="Passwod",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation",
                                widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
    def clean_email(self):
        """email validation method"""
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email
    def clean_password2(self):
        """password validation method"""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if not password1 or not password2:
            raise forms.ValidationError(u'Please confirm your password')
        if password1 != password2:
            raise forms.ValidationError(u'Password must match')
        return password2

class UserForm(forms.ModelForm):
    """Form to update User username in Profile"""
    class Meta:
        model = User
        fields = ('first_name','last_name','email')



class UserProfileForm(forms.ModelForm):
    """Form to update User Profile"""
    birth_date = DateField(
        widget=SelectDateWidget(years=previous_years(100))
    )
    reseller = BooleanField(required=False)
    class Meta:
        model = Userprofile
        fields = '__all__'
        

