from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from product.models import Product
from django.urls import reverse_lazy
from deals.models import Deals
from doctor.models import Doctor,Appointment
from django.views.generic import UpdateView,DetailView
from .forms import employeeform
from .forms import DoctorVisitsForm,ProductListForm,DealsDoneForm,editemployeeform,doctorListForm
from django.db.models import Sum,Count
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
#for dashboard and count of all
@login_required
def dashboard(request):
    products = Product.objects.all()
    product_count = products.count()

    Doctors = Doctor.objects.all()
    doctor_count = Doctors.count()

    deals = Deals.objects.all()
    deal_count = deals.count()

    employee = User.objects.all()
    employee_count = employee.count()



    context = {
        'product_count': product_count,
        'doctor_count':doctor_count,
        'deal_count':deal_count,
        'employee_count' :employee_count
    }
    return render(request,'base/index.html',context)

#for loginpage

def loginpage(request):
    return render(request,'base/login.html')



    
#function to add employee/user
@login_required
def add_employee(request):
    if request.method == "GET":
        form = employeeform()
        return render(request,'employee/addemployee.html',{'form_data':form})
    
    if request.method == "POST":
        form = employeeform(request.POST)
        print("inside if block")
        if form.is_valid():
            print("valid")
            form.save()
            
            messages.success(request,'Employee Added Successfully')
            return redirect('employee_list')
        else:
            form = employeeform()
        
    return render(request,'employee/addemployee.html',{'form_data':form})


        
    
#To view employee list
@login_required
def employee_list(request):
    all_items = User.objects.all()

    return render(request,'employee/viewemployee.html',{'items':all_items})



#To edit or update employee
@login_required
def editemployee(request,id):
    data = get_object_or_404(User, id=id)
    form = editemployeeform(instance=data)                                                               

    if request.method == "POST":
        form = editemployeeform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'Employee Updated Successfully')
            return redirect ('employee_list')
    return render(request, 'employee/editemployee.html', {'editemp': form}) 

class updateemployee(UpdateView):
    model = User
    form_class = editemployeeform
    template_name = 'employee/editemployee.html'
    success_url = reverse_lazy('employee_list')    



#To delete employee
@login_required
def delete_employee(request,id):
        pi = User.objects.get(id=id)
        pi.delete()
        messages.success(request,"Employee has been Successfully Delete")
        return redirect('employee_list')

#For No of doctor vists
@login_required
def doctor_visits_view(request):

    if request.method == 'POST':
        form = DoctorVisitsForm(request.POST)
        if form.is_valid():

            employee = form.cleaned_data['employee_name']
            month = form.cleaned_data['month']

            if month == 'All':
                visits_data = Appointment.objects.filter(Enteredby=employee).values('Enteredby').annotate(total_appointments=Count('id'))
                view_visits = Appointment.objects.filter(Enteredby=employee)
            else:
            
                visits_data = Appointment.objects.filter(Enteredby=employee, Date_of_schedule__month=month).values('Enteredby').annotate(total_appointments=Count('id'))
                view_visits = Appointment.objects.filter(Enteredby=employee,Date_of_schedule__month=month)
            return render(request, 'employee/doctorvisit.html', {'visits_data': visits_data, 'emp':employee.username,'view_visits':view_visits})

    else:
      
        form = DoctorVisitsForm()

    return render(request, 'employee/doctor_visits_form.html', {'form': form})


#deals done filter by employee name
@login_required
def dealsdone(request):
    if request.method == 'POST':
        form = DealsDoneForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee_name']
            month = form.cleaned_data['month']

            if month == 'All' :
                deals_data = Deals.objects.filter(Enteredby=employee).values('Enteredby').annotate(total_deals=Count('id'))
                deals_view = Deals.objects.filter(Enteredby=employee)
            else:
                deals_data = Deals.objects.filter(Enteredby=employee, Date__month=month).values('Enteredby').annotate(total_deals=Count('id'))
                deals_view = Deals.objects.filter(Enteredby=employee,Date__month=month)
            
            return render(request, 'employee/dealsdone.html', {'deals_data': deals_data, 'emp':employee.username,'deals_view':deals_view})

    else:
        form = DealsDoneForm()

    return render(request, 'employee/deals_done_form.html', {'form': form})

#filter products by employee 
@login_required
def productlist(request):
    if request.method == 'POST':
        form = ProductListForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee_name']
            
            
            products_data = Product.objects.filter(Enteredby=employee)
            
            return render(request, 'employee/productlist.html', {'products_data': products_data, 'emp':employee.username})

    else:
        form = ProductListForm()

    return render(request, 'employee/productlistf.html', {'form_data': form})

#filter doctors by employee
@login_required
def doctorlist(request):
    if request.method == 'POST':
        form = doctorListForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee_name']
            
            
            doctor_data = Doctor.objects.filter(Enteredby=employee)
            
            return render(request, 'employee/doctorlist.html', {'doctor_data': doctor_data, 'emp':employee.username})

    else:
        form = doctorListForm()

    return render(request, 'employee/doctorlistf.html', {'form_data': form})


#function to sort data
@login_required
def sort_fn(request):#firstname
     en = User.objects.all().order_by('first_name')
     context = {
         'data': en
     }
     return render(request,'employee/sort_data.html',context)
@login_required
def sort_ln(request):#lastname
    ln = User.objects.all().order_by('last_name')
    context = {
         'data': ln
     }
    return render(request,'employee/sort_data.html',context)
@login_required
def sort_un(request):#username
    un = User.objects.all().order_by('username')
    context = {
         'data': un
     }
    return render(request,'employee/sort_data.html',context)
@login_required
def sort_dj(request):#date of joined
    dj = User.objects.all().order_by('date_joined')
    context = {
         'data': dj
     }
    return render(request,'employee/sort_data.html',context)
    

class ProfileView(DetailView):
    model = User
    template_name = 'employee/profile.html'
    def get_user_profile(self, username):   
        profile_data = get_object_or_404(User, pk=username)
        return profile_data

           
       
            