from django.shortcuts import render
from products.models import Product
from helper.variables import background


def do_search(request):

    products = Product.objects.filter(name__icontains=request.GET['q'])
    selected_background = background["default"]
    return render(request, 'products.html', {"products":products, "background_image": selected_background})

