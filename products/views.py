from django.shortcuts import render, redirect, reverse
from helper.functions import get_categories_and_set_offer, get_products_for_carousel
from helper.variables import background
from .models import Product



def all_products(request):
    selected_background = background["default"]
    if request.method == "POST":
        category = request.POST["filter-by-category"]
        if category == "all_categories":
            products = Product.objects.all()
        else:
            products = Product.objects.filter(category=category)
            selected_background=background[category]
    else:
        products = Product.objects.all()
    categories = get_categories_and_set_offer(products)
    carousel_items = get_products_for_carousel(products)
    carousel_qty = len(carousel_items)
    return render(request, "products.html", { 
        "products": products, 
        "categories": categories, 
        "carousel_items": carousel_items, 
        "carousel_items_range": range(carousel_qty),
        "background_image": selected_background
        })


