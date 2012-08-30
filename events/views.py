from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import never_cache

from events.models import Event


@never_cache
def event_list(request):
    object_list = Event.upcoming.all
    if not object_list:
        raise Http404

    return render_to_response('events/event_list.html',
        {'object_list': object_list},
        context_instance=RequestContext(request))
