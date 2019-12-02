from django.db import models
from django.utils import timezone

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class UpcomingEventManager(models.Manager):
    def get_queryset(self):
        return super(UpcomingEventManager, self).get_queryset().filter(
            end_date__gte=timezone.now().date()
        )


class Event(models.Model):
    name = models.CharField(
        max_length=250,
        help_text='Maximum 250 characters.'
    )

    slug = models.SlugField(
        unique=True,
        help_text='Suggested value automatically generated from title. '
                  'Must be unique.'
    )

    start_date = models.DateField()
    end_date = models.DateField()

    url = models.URLField(blank=True)

    description = models.TextField()

    image = models.ImageField(
        upload_to='events',
        blank=True,
        help_text='80px X 80px'
    )

    image_alt_text = models.CharField(
        max_length=250,
        help_text='Describe the image as you would to someone over the phone. '
                  'Max length 250 characters.'
    )

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def get_absolute_url(self):
        return reverse('events:events_list')

    class Meta:
        ordering = ['start_date', 'end_date', 'name']

    def __unicode__(self):
        return self.name

    objects = models.Manager()  # default manager
    upcoming = UpcomingEventManager()
