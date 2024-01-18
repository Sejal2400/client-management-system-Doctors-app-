from django import forms
from django.contrib.auth.models import User
from .models import Product

#creating a form
class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields =['Product_name','Company_name','Product_image','Product_price']
        Product_name = forms.CharField(
            max_length=100,
            required=True,
            widget=forms.TextInput(attrs={'class':'form-control'})
        )

        Company_name = forms.CharField(
            max_length=100,
            required=True,
            widget=forms.TextInput(attrs={'class':'form-control'})
        )

        Product_image = forms.ImageField(
            required=True,
            widget=forms.ImageField()
        )

        Product_price = forms.FloatField(
            required=True,
            widget=forms.NumberInput(attrs={'class':'form-control'})

        )
        