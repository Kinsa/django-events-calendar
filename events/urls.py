from django.conf.urls import url

from events.feeds import UpcomingEvents
from events.views import event_list


app_name = 'events'

urlpatterns = [
    url(r'^feed/$', UpcomingEvents(), '', 'events_feed'),
    url(r'^$', event_list, {}, 'events_list'),
]
