from .variables import background
from django.utils import timezone

def previous_years(delta):
    current_year = timezone.now().year
    previous_year = current_year -delta -1
    return list(range(previous_year, current_year))

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