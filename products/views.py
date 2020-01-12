from django.shortcuts import render, redirect, reverse
from django.template.defaulttags import register
from django.shortcuts import get_object_or_404
from helper.functions import get_categories, get_products_for_carousel
from helper.variables import background
from .models import Product

@register.filter(name='with_name')
def with_name(value, arg):
    if arg in value :
        return value[arg]
    else:
        return value['default']

def all_products(request):
    selected_background = background["default"]
    if request.method == "POST":
        category = request.POST["filter-by-category"]
        if category == "all_categories":
            products = Product.objects.all()
        else:
            products = Product.objects.filter(category=category)
            if category in background:
                selected_background=background[category]
            else:
                selected_background=background["default"]
    else:
        products = Product.objects.all()
    categories = get_categories(products)
    carousel_items = get_products_for_carousel(products)
    carousel_qty = len(carousel_items)
    return render(request, "products.html", { 
        "products": products, 
        "categories": categories, 
        "carousel_items": carousel_items, 
        "carousel_items_range": range(carousel_qty),
        "background_image": background["main"],
        "background":background
        })

def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    selected_background = background[product.category]
    if product:
        return render(request, 
            "product-detail.html",
            {"product": product, 
            "background_image": selected_background})

