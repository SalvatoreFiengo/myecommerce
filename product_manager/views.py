from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from products.models import Product
from .forms import AddProductForm
from helper.variables import background

def get_vendor_products(request):
    """Create a view that will return 
    a list of products published by the user"""

    products = Product.objects.filter(vendor=request.user.id).order_by('-offer')
    user_product_form = AddProductForm()
    return render(request, "user_products.html", {"products":products, 
        "user_product_form": user_product_form, 
        "background_image":background["default"]})

def add_or_edit_a_product(request, pk=None):
    """Create a view that allows us to add or edit a product
    depending if the product ID(pk) is null or not"""

    all_products = Product.objects.filter(vendor=request.user.id).order_by('-offer')
    selected_product = get_object_or_404(Product, pk=pk) if pk else None
    edit = True if pk else False
    if request.method == "POST":
        if pk:
            user_product_form = AddProductForm(request.POST or None, request.FILES or None, instance=selected_product)
        else:
            user_product_form = AddProductForm(request.POST, request.FILES, instance=selected_product)
        if user_product_form.is_valid():
            selected_product = user_product_form.save(commit=False)
            selected_product.vendor = request.user
            selected_product.save()
            modal = False  
    else: 
        user_product_form = AddProductForm(instance=selected_product)
        modal = True
        
    return render(request, "user_products.html", {"products":all_products, 
        "user_product_form": user_product_form, 
        "background_image":background["default"],
        "modal": modal,
        "edit": edit
        })
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        selected = Product.objects.filter(pk=pk).delete()
        return redirect("user_products")
    else:
        return redirect("user_products")
