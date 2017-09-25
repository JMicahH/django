from django.conf.urls import url
from views import *
urlpatterns = [
    url(r'^$', index, name = 'index'),
    url(r'^register$', register, name = 'register_user'),
    url(r'^login$', login, name = 'login_user'),
    url(r'^welcome$', welcome, name = 'welcome_page')
]
