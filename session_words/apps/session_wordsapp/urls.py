from django.conf.urls import url
from views import *
urlpatterns = [
    url(r'^$', index, name = 'my_index'),
    url(r'^newword$', newword ),
    url(r'^clearsession', clearsession)
]
