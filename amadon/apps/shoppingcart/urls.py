from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name = 'my_index'),
    url(r'^purchase$', purchase ),
    url(r'^checkout$', checkout),
    url(r'^reset', reset)
]