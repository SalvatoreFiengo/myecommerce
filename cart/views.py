from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from products.models import Product
from django.contrib.auth.decorators import login_required
from helper.variables import background


@login_required
def view_cart(request):
    """A view that renders cart contents on the page"""
    return render(request, 'cart.html', {"background_image": background["main"]})


@login_required
def add_to_cart(request, id):
    """allows to add an item to the cart 
    if stock amount is not set throws error
    if quantity is not set provides default value"""
    product = get_object_or_404(Product, pk=id)
    quantity = request.POST.get('quantity')
    cart = request.session.get('cart', {})
    quantity = int(quantity) if quantity else 1
    if product.stock == 0:
        messages.warning(request, "{}, is not available at the moment".format(
            product.name), extra_tags="Not available")
        pass
    elif id in cart:
        cart[id] = int(cart[id]) + quantity
        request.session['cart'] = cart
    else:
        cart[id] = cart.get(id, quantity)
        request.session['cart'] = cart
    return redirect(reverse('products'))


def adjust_cart(request, id):
    """adjust quantity 
    of the specified product 
    to the specified amount"""
    quantity = request.POST.get('quantity')
    quantity = int(quantity) if quantity else None
    cart = request.session.get('cart', {})
    if quantity is None or quantity == cart[id]:
        pass
    elif quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def del_from_cart(request, id):
    """allows to add an item to the cart"""
    product = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
