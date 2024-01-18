from django import forms
from .models import Doctor
from .models import Appointment
import django.forms.utils
import django.forms.widgets
from django.forms.widgets import DateInput
from phonenumber_field.formfields import PhoneNumberField


class Doctorform(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['Doctor_name','Specialisation','Contact_number','Locations']
        Doctor_name = forms.CharField(
            max_length=100,
            required=True,
            widget=forms.TextInput(attrs={'class':'form-control'})
        )

        Specialisation = forms.CharField(
            max_length=100,
            required=True,
            widget=forms.TextInput(attrs={'class':'form-control'})
        )

        Contact_number = PhoneNumberField(
            
            required=False,
            widget=forms.NumberInput(attrs={'class':'form-control'})
        )

        Locations = forms.CharField(
            max_length=100,
            required=True,
            widget=forms.TextInput(attrs={'class':'form-control'})

        )

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class appointmentform(forms.ModelForm):
    Date_of_schedule = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd ', 'class': 'form-group'})
    )
    Time_of_schedule = forms.TimeField(widget=forms.widgets.TimeInput(
        attrs={'type':'time', 'class': 'form-group'}

    ))
    
    class Meta:
        model = Appointment

        fields = ['Doctor_name','Date_of_schedule','Time_of_schedule']

        Doctor_name = forms.CharField(
            max_length=100,
            required=True,
            widget=forms.TextInput(attrs={'class':'form-control'})
        )
        
        widgets = {'Time_of_schedule':forms.TimeInput(format='%H:%M'),
            
        }

        

        

        