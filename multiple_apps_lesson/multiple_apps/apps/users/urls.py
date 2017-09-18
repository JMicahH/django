from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name = 'my_index'),
    url(r'^register$', register, name = 'my_index'),
    url(r'^login$', login, name = 'my_index'),
    url(r'^new$', register, name = 'my_index'),
]