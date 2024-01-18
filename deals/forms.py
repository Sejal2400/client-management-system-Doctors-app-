from django import forms
from django.contrib.auth.models import User
from .models import Deals

class Dealsform(forms.ModelForm):
    Date = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd ', 'class': 'form-control'})
    )
    class Meta:
        model = Deals
        fields =['Doctor_name','Product_name','Quantity_ordered','Date']

        Doctor_name = forms.CharField(
            max_length=100,
            required=True,
            widget=forms.TextInput(attrs={'class':'form-control'})
        )
        Product_name = forms.CharField(
            max_length=100,
            required=True,
            widget=forms.TextInput(attrs={'class':'form-control'})
        )