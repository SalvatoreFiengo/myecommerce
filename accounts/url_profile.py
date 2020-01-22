from django.conf.urls import url, include
from accounts.views import user_profile, edit_profile, update_profile
from product_manager import urls as url_user_product

urlpatterns = [
    url(r'^$', user_profile, name="profile"),
    url(r'^edit_profile/$', edit_profile, name="edit_profile"),
    url(r'^edit_profile/', include(url_user_product)),
    url(r'^update_profile/$', update_profile, name="update_profile"),
]
