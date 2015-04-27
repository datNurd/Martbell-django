from django import forms
from django.contrib.auth.models import User
from .models import MerchantProfile

class MerchantForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')

class MerchantProfileForm(forms.ModelForm):
    class Meta:
        model = MerchantProfile
        fields = ('shop_name',)
