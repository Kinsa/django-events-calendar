import datetime
import markdown

from django.core.urlresolvers import reverse
from django.db import models

from sorl.thumbnail import ImageField


class UpcomingEventManager(models.Manager):

    def get_query_set(self):
        dr = datetime.date.today() + datetime.timedelta(weeks=12)
        return super(UpcomingEventManager, self).get_query_set().filter(
            start_date__gte=datetime.date.today(), start_date__lte=dr)


class Event(models.Model):
    name = models.CharField(max_length=250,
        help_text='Maximum 250 characters.')
    slug = models.SlugField(unique=True,
        help_text='Suggested value automatically generated from title. '\
                  'Must be unique.')

    start_date = models.DateField()
    end_date = models.DateField()

    url = models.URLField(blank=True)

    description = models.TextField(help_text="Use Markdown to mark this up.")
    description_html = models.TextField(editable=False, blank=True)

    image = ImageField(upload_to='events', blank=True, 
        help_text='80px X 80px')
    image_alt_text = models.TextField(max_length=250, help_text=''\
        'Describe the image as you would to someone over the phone. '\
        'Max length 250 characters.')

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def save(self, *args, **kwargs):
        self.description_html = markdown.markdown(self.description)
        super(Event, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('events')

    class Meta:
        ordering = ['start_date', 'end_date', 'name']

    def __unicode__(self):
        return self.name

    upcoming = UpcomingEventManager() # default manager
    objects = models.Manager()
