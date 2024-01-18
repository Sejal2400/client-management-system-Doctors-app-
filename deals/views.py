from django.shortcuts import render,redirect,get_object_or_404
from .models import Deals
from .forms import Dealsform
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required

# Create your views here.
#Function to add deals
@login_required
def add_deal(request):
    if request.method == 'POST': 
        fm = Dealsform(request.POST)
        if fm.is_valid():
            Deals = fm.save(commit=False)
            Deals.Enteredby = get_user(request)
            Deals.save()
           
            
            return redirect('deal_list')
            
        
    else:
        fm = Dealsform()

    return render(request,'deals/adddeals.html',{'form_data':fm})

#Function for listing deals
@login_required
def deal_list(request):
    deals = Deals.objects.all()
    userdeals = Deals.objects.filter(Enteredby=request.user)
    flag = deals.exists()
    data = {'deal_list': deals,
            'userdeals':userdeals,
            'flag':flag
            }

    return render(request,'deals/viewdeals.html',data)

#fuction for updating deals data
@login_required
def editdeals(request,id):
    data = get_object_or_404(Deals, id=id)
    form = Dealsform(instance=data)                                                               

    if request.method == "POST":
        form = Dealsform(request.POST, instance=data)
        if form.is_valid():
            form.save()

            return redirect ('deal_list')
    return render(request, 'deals/editdeals.html', {'form_data': form})

#Function for deleting deals record
@login_required
def delete_deals(request,id):
    deal = Deals.objects.get(id=id)
    deal.delete()
    messages.success(request,"Deal has been delete sucessfully")
    return redirect('deal_list')

#sort data
@login_required
def sort_docname(request):
    docname = Deals.objects.all().order_by('Doctor_name')

    context ={
        'data':docname
    }
    return render(request,'deals/sort_data.html',context)
@login_required
def sort_pname(request):
    pname = Deals.objects.all().order_by('Product_name')

    context ={
        'data':pname
    }
    return render(request,'deals/sort_data.html',context)
@login_required
def sort_quan(request):
    quan = Deals.objects.all().order_by('Quantity_ordered')

    context ={
        'data':quan
    }
    return render(request,'deals/sort_data.html',context)
@login_required
def sort_entby(request):
    entby = Deals.objects.all().order_by('Enteredby')

    context ={
        'data':entby
    }
    return render(request,'deals/sort_data.html',context)
@login_required
def sort_date(request):
    date = Deals.objects.all().order_by('Date')

    context ={
        'data':date
    }
    return render(request,'deals/sort_data.html',context)


