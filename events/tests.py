from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from events.models import Event

class EventTest(TestCase):
    fixtures = ['events.json']

    def setUp(self):
        self.client = Client()
    
    def test_add_event(self):

        self.assertEqual(Event.objects.all().count(), 5)
        self.assertEqual(Event.upcoming.all().count(), 2)
        self.assertEqual(Event.upcoming.all()[0].name, 'Current Event')
        self.assertEqual(Event.upcoming.all()[1].name, 'Near Future Event')
        
        r = self.client.get(reverse('events'))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'events/event_list.html')