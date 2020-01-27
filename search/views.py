from django.shortcuts import render, redirect, reverse
from products.models import Product
from helper.functions import get_products_for_carousel
from helper.variables import background, categories
from django.contrib import messages


def do_search(request):
    """search functionality based on string passed via GET form
    custom message if nothing is found"""
    products = Product.objects.filter(name__icontains=request.GET['q'])
    if not products:
        messages.error(
            request,
            "No products found with name: '" +
            request.GET['q']+"'",
            extra_tags="Search Result"
        )
        return redirect(reverse('products'))
    elif not request.GET['q']:
        messages.error(
            request,
            "No search query has been input, please try again",
            extra_tags="Search Result")
        return redirect(reverse('products'))
    else:
        selected_background = background["default"]
    current_categories = list(categories.values())
    carousel_items = get_products_for_carousel(products)
    carousel_qty = len(carousel_items)
    return render(request, "products.html", {
        "products": products,
        "categories": current_categories,
        "carousel_items": carousel_items,
        "carousel_items_range": range(carousel_qty),
        "background_image": selected_background,
        "background": background
    })
