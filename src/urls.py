from django.conf.urls.defaults import *

from ressaca.shortcuts import route
from ressaca.views import show_counter, inc_hangover_counter

urlpatterns = patterns('',

#    url(r'^$', show_counter, name='counter'),
#    url(r'^$', inc_hangover_counter, name='counter')
    route(r'^$', name='counter', GET=show_counter, POST=inc_hangover_counter)

)
