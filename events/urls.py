from django.conf.urls.defaults import patterns, url

from events.feeds import UpcomingEvents
from events.views import event_list


urlpatterns = patterns('',
    url(r'^feed/$', UpcomingEvents(), '', 'events_feed'),
    url(r'^$', event_list, {}, 'events'),
)
