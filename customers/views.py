# customers/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm,CustomerForm, RatingForm
from .models import Product,Customer
from django.db.models import Avg
from django.contrib.auth.decorators import permission_required,login_required

#Customer
@permission_required('auth.is_superuser')
@login_required
def customers_list(request):
    coustomers  = Customer.objects.all()
    return render(request, 'customer_list.html', {'coustomers': coustomers})

@permission_required('auth.is_superuser')
@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  
        form = CustomerForm()
    
    return render(request, 'customer_form.html', {'form': form})

@permission_required('auth.is_superuser')
@login_required
def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  
    else:
        form = CustomerForm(instance=customer)
    
    return render(request, 'customer_form.html', {'form': form})

@permission_required('auth.is_superuser')
@login_required
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')  
    
    return render(request, 'customer_confirm_delete.html', {'customer': customer})

#Product
@login_required
def product_list(request):
    products = Product.objects.annotate(avg_rating=Avg('rating__rating')).all()
    return render(request, 'product_list.html', {'products': products})

@permission_required('auth.is_superuser')
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  
    else:
        form = ProductForm()
    
    return render(request, 'product_form.html', {'form': form})

@permission_required('auth.is_superuser')
@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'product_form.html', {'form': form})

@permission_required('auth.is_superuser')
@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list') 
    
    return render(request, 'product_confirm_delete.html', {'product': product})

@login_required
def add_rating(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  
    else:
        form = RatingForm()
    
    return render(request, 'rating_form.html', {'form': form})