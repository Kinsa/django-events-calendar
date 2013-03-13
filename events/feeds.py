from django.template.defaultfilters import striptags
from django.contrib.syndication.views import Feed

from events.models import Event


class UpcomingEvents(Feed):
    title = 'Events'
    link = '/events/'
    description = 'Upcoming events'

    def items(self):
        return Event.upcoming.all()[:30]

    def item_pubdate(self, item):
        return item.created

    def item_title(self, item):
        return striptags(item.name)

    def item_description(self, item):
        return item.description
