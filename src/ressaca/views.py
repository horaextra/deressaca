from django.template import RequestContext
from django.shortcuts import render_to_response

def show_counter(request):

    context = RequestContext(request)

    return render_to_response('index.html', context)

