
from django import forms 
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class employeeform(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2','email','is_active','date_joined']
    
    username = forms.CharField(
        max_length= 100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}
        )
    )
    
    email = forms.EmailField(
        max_length= 100,
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control'}
        )
    )
    
    first_name = forms.CharField(
        max_length= 100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}
        )
    )
    
    last_name = forms.CharField(
        max_length= 100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}
        )
    )
    
    password1 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','type':'password'}
    )
    
    )
    
    password2 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','type':'password'}
    )
    
    )
    date_joined = forms.DateField(widget=forms.widgets.DateInput(
        
        attrs={'type': 'date', 'class': 'form-control'})
    )
    




class DoctorVisitsForm(forms.Form):
    employee_name = forms.ModelChoiceField(queryset=User.objects.all())
    month = forms.ChoiceField(choices=[('All', 'All'),(1, 'January'), (2, 'February'), (3,'March'),(4,'April'),(5,'May'),(6,'June'),(7,'July'),(8,'August'),(9,'September'),(10,'October'),(11,'November'),(12,'December')])


class DealsDoneForm(forms.Form):
    employee_name = forms.ModelChoiceField(queryset=User.objects.all())
    month = forms.ChoiceField(choices=[('All', 'All'),(1, 'January'), (2, 'February'), (3,'March'),(4,'April'),(5,'May'),(6,'June'),(7,'July'),(8,'August'),(9,'September'),(10,'October'),(11,'November'),(12,'December')])  


class ProductListForm(forms.Form):
    employee_name = forms.ModelChoiceField(queryset=User.objects.all())

class doctorListForm(forms.Form):
    employee_name = forms.ModelChoiceField(queryset=User.objects.all())



class editemployeeform(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','is_active','date_joined']
    
   
    
    email = forms.EmailField(
        max_length= 100,
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control'}
        )
    )
    
    first_name = forms.CharField(
        max_length= 100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}
        )
    )
    
    last_name = forms.CharField(
        max_length= 100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}
        )
    )
    
    
    
    
    date_joined = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'class': 'form-control'})
    )
    






        


        
