from django.shortcuts import render, redirect, reverse
from .models import Product

def all_products(request):
    products = Product.objects.all()
    categories = []
    for product in products:
        categories.append(product.category)
        if product.offer > 0:
            offer_amount = (product.price/100)*product.offer
            product.discount = product.price - offer_amount
            product.discount = "%.2f" % product.discount
            product.save()
    return render(request, "products.html", { "products": products, "categories": categories })

def filter_product_by_category(request):
    if request.method == "POST":
        all_products = Product.objects.all()
        categories = []
        selected_category = request.POST["filter-by-category"]
        if selected_category == "all_categories":
            return redirect(reverse("products"))
        else:
            for product in all_products:
                categories.append(product.category)
            
            filtered_products = Product.objects.filter(category=request.POST["filter-by-category"])
        
            return render(request, "products.html", {"products": filtered_products, "categories": categories})
    else:
        return redirect(reverse("products"))