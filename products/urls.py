from django.conf.urls import url
from .views import all_products, product_details

urlpatterns = [
    url(r'^$', all_products, name="products"),
    url(r'^product/(?P<pk>\d+)/', product_details, name="product_details")
]