from django.conf.urls import url
from views import *
urlpatterns = [
    url(r'^$', index, name = 'my_index'),
    url(r'^new$', new, name = 'add_user_page'),
    url(r'^creation$', creation, name = 'create_user'),
    url(r'^(?P<id>\d+)/show$', show, name = 'show_user'),
    url(r'^(?P<id>\d+)/edit$', edit, name = 'edit_user'),
    url(r'^update$', update, name = 'update_user'),
    url(r'^(?P<id>\d+)/delete$', delete, name = 'delete_user'),
]