from django.conf.urls import url
from .views import get_vendor_products, add_or_edit_a_product, delete_product

urlpatterns = [
    url('^your_products/$', get_vendor_products, name="user_products"),
    url('^your_products/$', add_or_edit_a_product, name="add_product"),
    url('^your_products/add/$', add_or_edit_a_product, name="edit_selected_product"),
    url('^your_products/(?P<pk>\d+)/edit/$', add_or_edit_a_product, name="edit_selected_product"),
    url('^your_products/(?P<pk>\d+)/delete/$', delete_product, name="delete_product"),
]