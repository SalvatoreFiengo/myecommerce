from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart, del_from_cart

urlpatterns = [
    url(r'^$', view_cart, name="view_cart"),
    url(r'^add/(?P<id>\d+)', add_to_cart, name="add_to_cart"),
    url(r'^del/(?P<id>\d+)', del_from_cart, name="del_from_cart"),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name="adjust_cart")
]