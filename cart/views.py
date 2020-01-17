from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from products.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def view_cart(request):
    """A view that renders cart contents on the page"""
    return render(request, 'cart.html')

@login_required
def add_to_cart(request, id):
    """allows to add an item to the cart"""
    product = get_object_or_404(Product, pk=id)
    quantity = request.POST.get('quantity') 
    cart = request.session.get('cart', {})
    if not quantity: quantity = 0
    else:
        quantity = int(quantity)
        if id in cart:
            cart[id] = int(cart[id]) + quantity
        else:
            cart[id] = cart.get(id, quantity)
            request.session['cart'] = cart
    return redirect(reverse('products'))


def adjust_cart(request, id):
    """adjust quantity 
    of the specified product 
    to the specified amount""" 
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity >0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart

    return redirect(reverse('view_cart'))