import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from events.models import Event


class EventTest(TestCase):

    fixtures = ['test_data_events.json']

    def setUp(self):
        self.client = Client()

    def test_event_routing(self):
        today = datetime.date.today()

        # Update the fixture dates
        ce = Event.objects.get(name='Current Event')
        ce.start_date = today
        ce.end_date = today + datetime.timedelta(days=1)
        ce.save()

        nfe = Event.objects.get(name='Near Future Event')
        nfe.start_date = today + datetime.timedelta(weeks=2)
        nfe.end_date = today + datetime.timedelta(days=2, weeks=2)
        nfe.save()

        # Test that we now have 2 upcoming / ongoing events and 5 total events
        self.assertEqual(Event.objects.all().count(), 5)
        self.assertEqual(Event.upcoming.all().count(), 2)
        self.assertEqual(Event.upcoming.all()[0].name, 'Current Event')
        self.assertEqual(Event.upcoming.all()[1].name, 'Near Future Event')

        # Test that the event_list template is used
        r = self.client.get(reverse('events'))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'events/event_list.html')

        # Test that only upcoming events show up in the template
        for event in Event.upcoming.all():
            self.assertContains(r, event.name)
        for event in Event.objects.all():
            if not event.name == 'Current Event' \
                    and not event.name == 'Near Future Event':
                self.assertNotContains(r, event.name)
