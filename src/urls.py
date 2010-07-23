from django.conf.urls.defaults import *

urlpatterns = patterns('',

    (r'^$', 'ressaca.views.show_counter'),

)
