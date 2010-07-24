#coding:utf-8
from datetime import datetime

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import Hangover

@require_GET
def show_counter(request):
    hangovers = Hangover.objects.count()

    context = RequestContext(request, {'hangovers':hangovers})
    return render_to_response('index.html', context)

@require_POST
def inc_hangover_counter(request):
    twitter_message = 'Eu também estou #deressaca!'
    twitter_url = 'http://twitter.com/?status=%s' % twitter_message

    if 'new_hangover' in request.POST:
        Hangover.objects.create()

        return HttpResponseRedirect(twitter_url)
    else:
        return HttpResponseRedirect(reverse('counter'))
