from django.conf.urls.defaults import *

from ressaca.shortcuts import route
from ressaca.views import show_counter

urlpatterns = patterns('',

    route(r'^$', name='counter', GET=show_counter)

)
