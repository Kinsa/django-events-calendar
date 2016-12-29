from django.http import Http404
from django.shortcuts import render
from django.views.decorators.cache import never_cache

from events.models import Event


@never_cache
def event_list(request):
    object_list = Event.upcoming.all
    if not object_list:
        raise Http404

    return render(
        request,
        template_name='events/event_list.html',
        context={'object_list': object_list}
    )
