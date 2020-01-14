from django.conf.urls import url, include
from accounts.views import user_profile, edit_profile, update_profile

urlpatterns = [
    url(r'^', user_profile, name="profile"),
    url(r'^edit_profile/', edit_profile, name="edit_profile"),
    url(r'^', update_profile, name="update_profile"),
]
