=============
Django Events
=============

A simple upcoming events calendar for Django.

Installation from Source
========================

::

 $ git clone git://github.com/jbergantine/django-events.git
 $ cd django-events
 $ python setup.py install

Installation via PIP Requirements File
======================================

Include in the PIP requirements file the following lines:

::

 -e git://github.com/jbergantine/django-events.git#egg=events

And then install as normal (IE:)

::

 $ pip install -r path/to/requirements/file.txt

Setup the Project For the Application
=====================================

Add to the project's settings file tuple of INSTALLED_APPS:

::

 'events',
 'sorl.thumbnail',

If you're using South, initiate the events application.

::

 $ python manage.py schemamigration events --auto

Sync the database to finish installing sorl-thumbnail and events if you aren't using South.

::

 $ python manage.py syncdb

If you're using South, migrate the events application to finish installing it.

::

 $ python manage.py migrate events

In the project's urls.py file add:

::

 url(r'^events/', include('events.urls')),

A list of upcoming events can now be linked to:

::

 <a href="{% url 'events' %}">Events</a>

The RSS feed of upcoming events can now be referred to in the ``<head>`` of your HTML templates:

::

 <link rel="feed alternate" type="application/rss+xml" title="Events" href="{% url 'events_feed' %}" />

Configure the Templates
=======================

By default the templates contain only the bare necessities. To override the default templates, create a directory called events in your templates directory and copy the templates from the project into that directory in order to make adjustments to them. If you're using Virtualenv, ``cd`` to the root of the django project and execute the following command:

::

 cp -r $VIRTUAL_ENV/src/django-events/events/templates/events templates/events
