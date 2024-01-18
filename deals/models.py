from django.db import models
from employee.models import Employee
from product.models import Product
from doctor.models import Doctor
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.

class Deals(models.Model):
    Doctor_name = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Product_name = models.ForeignKey(Product,on_delete=models.CASCADE)
    Quantity_ordered = models.PositiveIntegerField(validators=[MinValueValidator(10)])
    Date = models.DateField(validators=[MinValueValidator(datetime.date.today)])
    Enteredby = models.ForeignKey(User,on_delete=models.CASCADE)



    