import datetime

from django.test import TestCase
from django.test.client import Client

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from django.utils import timezone

from events.models import Event


class EventTest(TestCase):
    fixtures = ['test_data_events.json']

    def setUp(self):
        self.client = Client()

    def test_event_routing(self):
        today = timezone.now().today()

        # Update the fixture dates
        ce = Event.objects.get(name='Current Event')
        ce.start_date = today
        ce.end_date = today + datetime.timedelta(days=1)
        ce.save()

        nfe = Event.objects.get(name='Near Future Event')
        nfe.start_date = today + datetime.timedelta(weeks=2)
        nfe.end_date = today + datetime.timedelta(days=2, weeks=2)
        nfe.save()

        ffe = Event.objects.get(name='Far Future Event')
        ffe.start_date = today + datetime.timedelta(weeks=42)
        ffe.end_date = today + datetime.timedelta(days=2, weeks=42)
        ffe.save()

        fpe = Event.objects.get(name='Far Past Event')
        fpe.start_date = today - datetime.timedelta(days=2, weeks=42)
        fpe.end_date = today - datetime.timedelta(weeks=42)
        fpe.save()

        npe = Event.objects.get(name='Near Past Event')
        npe.start_date = today - datetime.timedelta(days=2, weeks=2)
        npe.end_date = today - datetime.timedelta(weeks=2)
        npe.save()

        # Test that we now have 3 upcoming / ongoing events and 5 total events
        self.assertEqual(Event.objects.all().count(), 5)
        self.assertEqual(Event.upcoming.all().count(), 3)
        self.assertEqual(Event.upcoming.all()[0].name, 'Current Event')
        self.assertEqual(Event.upcoming.all()[1].name, 'Near Future Event')
        self.assertEqual(Event.upcoming.all()[2].name, 'Far Future Event')

        # Test that the event_list template is used
        r = self.client.get(reverse('events:events_list'))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'events/event_list.html')

        # Test that only upcoming events show up in the template
        for event in Event.upcoming.all():
            self.assertContains(r, event.name)
        for event in Event.objects.all():
            if not event.name == 'Current Event' \
                    and not event.name == 'Near Future Event' \
                    and not event.name == 'Far Future Event':
                self.assertNotContains(r, event.name)

        # Test the event feed
        rf = self.client.get(reverse('events:events_feed'))
        self.assertEqual(rf.status_code, 200)
