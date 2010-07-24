from django.conf.urls.defaults import *
from django.conf import settings

from ressaca.shortcuts import route
from ressaca.views import show_counter, inc_hangover_counter

urlpatterns = patterns('',

    route(r'^$', name='counter', GET=show_counter, POST=inc_hangover_counter),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}
    )

)
