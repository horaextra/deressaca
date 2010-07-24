from datetime import datetime

from django.template import RequestContext
from django.shortcuts import render_to_response

from models import Hangover

def show_counter(request):
    hangover = Hangover.objects.create(counter=0)

    context = RequestContext(request, {'hangovers':hangover.counter})

    return render_to_response('index.html', context)

