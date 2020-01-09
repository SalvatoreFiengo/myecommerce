"""importing necessary modules from django"""
from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, edit_profile, update_profile
from accounts import url_reset

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^profile/$', user_profile, name="profile"),
    url(r'^edit_profile/$', edit_profile, name="edit_profile"),
    url(r'^$', update_profile, name="update_profile"),
    url(r'^password_reset/', include(url_reset), name="password_reset")
]
