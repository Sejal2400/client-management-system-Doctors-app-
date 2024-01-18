from django.shortcuts import render,redirect,get_object_or_404
from .models import Doctor
from .models import Appointment
from .forms import Doctorform
from .forms import appointmentform
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
#Function to add doctor
@login_required
def add_doctor(request):
    if request.method == 'POST': 
        fm = Doctorform(request.POST)
        if fm.is_valid():
            Doctor = fm.save(commit=False)
            Doctor.Enteredby = get_user(request)
            Doctor.save()
            messages.success(request,"Doctor Added Successfully")
           
            
            return redirect('doctor_list')
            
        
    else:
        fm = Doctorform()

    return render(request,'doctor/adddoctor.html',{'form_data':fm})

#Function for listing doctor
@login_required
def doctor_list(request):
    all_items = Doctor.objects.all()
    userdoctor = Doctor.objects.filter(Enteredby=request.user)
    flag = all_items.exists()
    data = { 'items':all_items ,
            'userdoctor':userdoctor ,
            'flag':flag

            }

    return render(request,'doctor/viewdoctor.html',data)

#fuction for updating data
@login_required
def editdoctor(request,id):
    data = get_object_or_404(Doctor, id=id)
    form = Doctorform(instance=data)                                                               

    if request.method == "POST":
        form = Doctorform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,"Doctor Updated Successfully")
            return redirect ('doctor_list')
    return render(request, 'doctor/editdoctor.html', {'form_data': form})

#Function for deleting doctor record

'''def delete_doctor(request,id):
    if request.method =='POST':
        doc = Doctor.objects.get(id=id)
        doc.delete()
        messages.success(request,"Doctor Removed Successfully")
    return redirect('doctor_list')  '''
@login_required
def delete_doctor(request,id):
        doc = Doctor.objects.get(id=id)
        doc.delete()
        messages.success(request,"Doctor has been removed successfully")
        return redirect('doctor_list')


#functions to sort data
@login_required
def sort_dn(request):
    dn = Doctor.objects.all().order_by('Doctor_name')

    context ={
        'data':dn
    }
    return render(request,'doctor/sort_data.html',context)
@login_required
def sort_sp(request):
    sp = Doctor.objects.all().order_by('Specialisation')

    context ={
        'data':sp
    }
    return render(request,'doctor/sort_data.html',context)
@login_required
def sort_lo(request):
    lo = Doctor.objects.all().order_by('Locations')

    context ={
        'data':lo
    }
    return render(request,'doctor/sort_data.html',context)
@login_required
def sort_eb(request):
    eb = Doctor.objects.all().order_by('Enteredby')

    context ={
        'data':eb
    }
    return render(request,'doctor/sort_data.html',context)


#------------------------------------------------------------------------------
@login_required
def add_appointment(request):
    if request.method == 'POST': 
        fm = appointmentform(request.POST)
        if fm.is_valid():
            Appointment = fm.save(commit=False)
            Appointment.Enteredby = get_user(request)
            Appointment.save()
            messages.success(request,"Appointment Added Successfully")
           
            
            return redirect('appointment_list')
            
        
    else:
        fm = appointmentform()

    return render(request,'doctor/addappointment.html',{'form_data':fm})


#Function for listing doctor
@login_required 
def appointment_list(request):
    all_items = Appointment.objects.all()
    userappoinment = Appointment.objects.filter(Enteredby=request.user)
    flag = all_items.exists()
    data = { 'items':all_items ,
            'userappoinment':userappoinment ,
            'flag':flag

            }
    
    return render(request,'doctor/viewappointment.html',data)


#function for updating the appointment
@login_required
def editappointment(request,id):
    data = get_object_or_404(Appointment, id=id)
    form = appointmentform(instance=data)                                                               

    if request.method == "POST":
        form = appointmentform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,"Appointment Updated Successfully")
            return redirect ('appointment_list')
    return render(request, 'doctor/editappointment.html', {'form_data': form})


@login_required
def delete_appointment(request,id):
        apo = Appointment.objects.get(id=id)
        apo.delete()
        messages.success(request,"Appointment Removed Successfully")
    
        return redirect('appointment_list')
    

#function for todays 
@login_required
def todaysschedule(request):
    today = datetime.now().date()
    data  = Appointment.objects.filter(Date_of_schedule=today)
    context={
            'object':data
        }
    return render(request,'doctor/todayschedule.html',context)

#function to sort data
@login_required
def sort_adn(request):
    adn = Appointment.objects.all().order_by('Doctor_name')

    context ={
        'data':adn
    }
    return render(request,'doctor/sortdata.html',context)
@login_required
def sort_ds(request):
    ds = Appointment.objects.all().order_by('Date_of_schedule')

    context ={
        'data':ds
    }
    return render(request,'doctor/sortdata.html',context)
@login_required
def sort_en(request):
    en = Appointment.objects.all().order_by('Enteredby')

    context ={
        'data':en
    }
    return render(request,'doctor/sortdata.html',context)




