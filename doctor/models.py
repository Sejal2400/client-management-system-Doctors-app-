from django.db import models
from employee.models import Employee
from django.contrib.auth.models import User
import datetime
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Doctor(models.Model):
    type = (("Neurology","Neurology"),("Cardiology","Cardiology"),("General","General"),("Orthopaedic","Orthopaedic"),("Urology","Urology"),("Pediatrics","Pediatrics"),("gynecologists,","gynecologists,"),("dentists","dentists"))
    Doctor_name = models.CharField(max_length=70)
    Specialisation = models.CharField(max_length=70,choices=type)
    phone_regex = RegexValidator(regex=r'[6-9][0-9]{9}')
    Contact_number = models.CharField(validators=[phone_regex],max_length=10)
    Locations = models.CharField(max_length=80)
    Enteredby = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.Doctor_name
    
class Appointment(models.Model):
    Doctor_name = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Date_of_schedule = models.DateField(validators=[MinValueValidator(datetime.date.today)])
    Time_of_schedule = models.TimeField()
    Enteredby = models.ForeignKey(User,on_delete=models.CASCADE)
