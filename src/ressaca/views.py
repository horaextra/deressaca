from datetime import datetime

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.http import require_GET, require_POST

from models import Hangover

@require_GET
def show_counter(request):
    hangover = Hangover.objects.create(counter=0)

    context = RequestContext(request, {'hangovers':hangover.counter})
    return render_to_response('index.html', context)

@require_POST
def inc_hangover_counter(request):
    if 'new_hangover' in request.POST:
        hangover = Hangover.objects.create(counter=1)
        context = RequestContext(request, {'hangovers':hangover.counter})
        return render_to_response('index.html', context)

