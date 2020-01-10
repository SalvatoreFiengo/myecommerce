from django.shortcuts import render, redirect, reverse
from .models import Product

def get_products_for_carousel(products):
    showlist = []
    for product in products:
        if product.offer > 0:
            showlist.append(product)
    carousel_items = sorted(showlist, key=lambda product: product.discount, reverse=True)
    return carousel_items

def get_categories_and_set_offer(products):
    categories = []
    for product in products:
        categories.append(product.category)
        if product.offer > 0:
            offer_amount = (product.price/100)*product.offer
            product.discount = product.price - offer_amount
            product.discount = "%.2f" % product.discount
            product.save()
    return categories

def all_products(request):
    background = '/media/images/background.jpg'
    products = Product.objects.all()
    categories = get_categories_and_set_offer(products)
    carousel_items = get_products_for_carousel(products)
    carousel_qty = len(carousel_items)
    return render(request, "products.html", { 
        "products": products, 
        "categories": categories, 
        "carousel_items": carousel_items, 
        "carousel_items_range": range(carousel_qty),
        "background_image": background
        })

def filter_product_by_category(request):
    background = '/media/images/background.jpg'
    if request.method == "POST":
        all_products = Product.objects.all()
        categories = []
        selected_category = request.POST["filter-by-category"]
        if selected_category == "all_categories":
            return redirect(reverse("products"))
        else:

            category = request.POST["filter-by-category"]
            for product in all_products:
                categories.append(product.category)
            
            filtered_products = Product.objects.filter(category=category)
        
            return render(request, "products.html", {"products": filtered_products, "categories": categories, "background_image": background})
    else:
        return redirect(reverse("products"))

