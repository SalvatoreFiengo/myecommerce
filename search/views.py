from django.shortcuts import render, redirect, reverse
from products.models import Product
from helper.variables import background, categories
from django.contrib import messages


def do_search(request):
    """search functionality based on string passed via GET form
    custom message if nothing is found"""
    products = Product.objects.filter(name__icontains=request.GET['q'])
    if not products:
        messages.error(request, "No products found with name: '"+request.GET['q']+"'", extra_tags="Search Result")
        return redirect(reverse('products'))
    else:
        selected_background = background["default"]
        selected_categories = list(categories.values())
        return render(request, 'products.html', {"products":products, 
            "background_image": selected_background, "categories": selected_categories})

