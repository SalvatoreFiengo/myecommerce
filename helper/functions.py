from .variables import background
from django.utils import timezone


def previous_years(delta):
    """
    given an int provides a range of years based on delta -1 
    """
    current_year = timezone.now().year
    previous_year = current_year - delta - 1
    return list(range(previous_year, current_year))


def get_products_for_carousel(products):
    """filters and sorts products based on discount if products have offer set greater than zero"""
    showlist = []
    for product in products:
        if product.offer > 0:
            showlist.append(product)
    carousel_items = sorted(
        showlist, key=lambda product: product.discount, reverse=True)
    return carousel_items
