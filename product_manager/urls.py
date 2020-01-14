from django.conf.urls import url
from .views import get_vendor_products, add_or_edit_a_product

urlpatterns = [
    url('^your_products/$', get_vendor_products, name="user_products"),
    url('^your products/$', add_or_edit_a_product, name="edit_user_products"),
    url('^(?P<pk>\d+)/edit/$', get_vendor_products, name="edit_a_products"),
]