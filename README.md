=============
Django Events
=============

A simple upcoming events calendar for Django.

[![TravisCI Build Status](https://travis-ci.org/jbergantine/django-events.svg?branch=develop)](https://travis-ci.org/jbergantine/django-events)

Installation via PIP
====================

```sh
$ pip install -e git://github.com/jbergantine/django-events.git#egg=events
```

Installation from Source
========================

```sh
$ git clone git://github.com/jbergantine/django-events.git
$ cd django-events
$ python setup.py install
```

Usage
=====

### Setup the Project For the Application

Add to the `INSTALLED_APPS` tuple in the project's settings file:

```py
'sorl.thumbnail',
'events',
```

In the project's urls.py file add:

```py
from django.conf.urls import include
...
url(r'^events/', include('events.urls', namespace='events')),
```

A list of upcoming events can now be linked to:

```html
<a href="{% url 'events:events_list' %}">Events</a>
```

The RSS feed of upcoming events can now be referred to in the ``<head>`` of your HTML templates:

```html
<link rel="feed alternate" type="application/rss+xml" title="Events" href="{% url 'events:events_feed' %}" />
```

### Configure the Templates

By default the templates contain only the bare necessities. To override the default templates, create a directory called events in your templates directory and copy the templates from the project into that directory in order to make adjustments to them. If you're using VirtualEnv, `cd` to the root of the Django project and execute the following command:

```sh
$ cp -r $VIRTUAL_ENV/src/django-events/events/templates/events templates/events
```

Testing
=======

```sh
$ python setup.py test
```

### With TOX

First, install Tox, then run the tests. This will test against the Django versions specified in the environments specified in the ``tox.ini`` file

```sh
$ pip install tox
$ tox
```

Releasing
=========

Before releasing, rebuild the readme file as a reStructuredTxt file using [pandoc](http://pandoc.org). Pandoc will need to be installed on the system first.

```sh
$ pandoc --from=markdown --to=rst --output=README.rst README.md
```
