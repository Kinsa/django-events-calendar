## Installation

    $ pip install -r requirements.txt

## Usage

Add ``'events',`` to the ``INSTALLED_APPS`` tuple in ``settings.py``.

Add ``'sorl.thumbnail',`` to the ``INSTALLED_APPS`` tuple in ``settings.py``.

Sync the database to finish installing sorl-thumbnail.

Migrate the database to finish installing events.

Add the following to the ``patterns()`` method in the project's primary ``urls.py`` file:

    url(r'^events/', include('events.urls')),
    
The event list can now be referred to with the url 'events':

    <a href="{% url 'events' %}">Events</a>

The RSS feed can now be referred to in the ``<head>`` of your HTML templates:
    
    <link rel="feed alternate" type="application/rss+xml" title="Events" href="{% url events_feed %}" />

Edit the templates as necessary.