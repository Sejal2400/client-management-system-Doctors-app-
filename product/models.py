from django.db import models
from employee.models import Employee
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Product(models.Model):
    Product_name = models.CharField(max_length=100)
    Company_name = models.CharField(max_length=100)
    Product_image = models.ImageField(upload_to="media")
    Product_price = models.FloatField(validators=[MinValueValidator(5.0)])
    Enteredby = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Product_name
