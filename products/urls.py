from django.conf.urls import url
from .views import all_products
from .views import filter_product_by_category

urlpatterns = [
    url(r'^$', all_products, name="products"),
    url(r'^filtered/$', filter_product_by_category, name="filtered"),
]