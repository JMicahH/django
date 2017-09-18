from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'^$', index, name = 'my_index'),
    url(r'^new$', new, name = 'my_index'),
    url(r'^create$', create, name = 'my_index'),
    url(r'^(?P<number>\d+)$', show, name = 'my_index'),
    url(r'^(?P<number>\d+)/edit$', edit, name = 'my_index'),
    url(r'^(?P<number>\d+)/delete$', destroy, name = 'my_index'),
]