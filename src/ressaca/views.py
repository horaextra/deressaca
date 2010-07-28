#coding:utf-8
import urllib
from datetime import datetime

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import Hangover

@require_GET
def show_counter(request):
    today = datetime.today().date()
    hangovers = str(len(Hangover.objects.filter(day=today)))
    hangovers = '0' * (4 - len(hangovers)) + hangovers

    context = RequestContext(request, {'hangovers':hangovers})
    return render_to_response('index.html', context)

@require_POST
def inc_hangover_counter(request):
    msg = 'Eu também estou #deressaca! http://deressaca.net'
    twitter_message = urllib.urlencode({'status': msg})
    twitter_url = 'http://twitter.com/home?%s' % twitter_message

    if 'new_hangover' in request.POST:
        Hangover.objects.create()

        return HttpResponseRedirect(twitter_url)
    else:
        return HttpResponseRedirect(reverse('counter'))
