from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse,get_object_or_404
from .models import Product
from django.http import Http404
from .forms import Productform
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required





# Create your views here.

@login_required
def product_list(request):
    products = Product.objects.all()
    eproducts =  Product.objects.filter(Enteredby=request.user)
    flag = products.exists()
    data = {'product_list': products,
            'eproducts':eproducts,
            'flag':flag
            }

    return render(request,'product/viewproduct.html',data)

#classbased view to Add product

class createproduct(CreateView):
    model = Product 
    fields = ['Product_name','Company_name','Product_image','Product_price','Enteredby']
    
    
    def get_success_url(self):
        return reverse_lazy('product_list')
    


#Function to Add product 
@login_required  
def productadd(request):
    if request.method == 'POST':
        form = Productform(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            product = form.save(commit=False)
            product.Enteredby = get_user(request)
            product.save()
            messages.success(request,'Product Added  Successfully')
            return redirect('product_list')
        #else:
            #print(form.errors)  # Print form errors to the console for debugging purposes
            #return HttpResponse("Form is not valid. Errors: {}".format(form.errors))
                
    else:
        form = Productform()
    return render(request, 'product/newproduct.html', {'form_data': form})


#this Function is for update or edit
@login_required
def editproduct(request,id):
    data = get_object_or_404(Product, id=id)
    form = Productform(instance=data)                                                               

    if request.method == "POST":
        form = Productform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'Product Updated Successfully')
            return redirect ('product_list')
    return render(request, 'product/editproduct.html', {'form_data': form})


        


#fuction for deleting the Product
@login_required
def delete_data(request,id):
    pi = Product.objects.get(id=id)
    pi.delete()
    messages.success(request,"Product has been removed successfully")
    return redirect('product_list')
    


#To count no. of product in the database
# def count_products(request):
#     products = Product.objects.all()
#     product_count = products.count()
#     return render(request,'base/index.html',{'product_count': product_count})



#to Sort data
@login_required
def sort_pn(request):
    pn = Product.objects.filter(Enteredby=request.user).order_by('Product_name')

    context ={
        'data':pn
    }
    return render(request,'product/sort_data.html',context)

@login_required
def sort_cn(request):
    cn = Product.objects.filter(Enteredby=request.user).order_by('Company_name')
    context ={
        'data':cn
    }
    return render(request,'product/sort_data.html',context)

@login_required
def sort_pp(request):
    pp = Product.objects.filter(Enteredby=request.user).order_by('Product_price')

    context ={
        'data':pp
    }
    return render(request,'product/sort_data.html',context)
@login_required
def sort_eb(request):
    eb = Product.objects.all().order_by('Enteredby')

    context ={
        'data':eb
    }
    return render(request,'product/sort_data.html',context)
  


    




    
    








