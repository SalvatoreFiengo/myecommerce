from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, \
    password_reset_confirm, password_reset_complete
from helper.variables import background


urlpatterns= [
    url(r'^$', password_reset, {"extra_context":{"background_image":"media/images/white-background.jpg"},'post_reset_redirect': reverse_lazy('password_reset_done')}, name="password_reset"),
    url(r'^done$', password_reset_done, {"extra_context":{"background_image":"media/images/white-background.jpg"}},name="password_reset_done"),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {"extra_context":{"background_image":"media/images/white-background.jpg"},'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    url(r'^complete$', password_reset_complete,{"extra_context":{"background_image":"media/images/white-background.jpg"}}, name="password_reset_complete"),
]

