from django.conf.urls import url, include
from accounts.views import logout, login, registration
from accounts import url_reset
from accounts import url_profile

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^profile/', include(url_profile), name="profile"),
    url(r'^password_reset/', include(url_reset), name="password_reset")
]
