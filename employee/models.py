from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employee(models.Model):
    status_type = (('Active','Active'),('Inactive','Inactive'))
    First_name = models.CharField(max_length=70)
    Last_name = models.CharField(max_length=70)
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    Email = models.EmailField()
    Password = models.CharField(max_length=30)
    Date_of_joining = models.DateField()
    Status = models.CharField(max_length=30,choices=status_type)

    def __str__(self) :
        return (self.First_name + self.Last_name)

    
   
    




