# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, help_text='Maximum 250 characters.')),
                ('slug', models.SlugField(unique=True, help_text='Suggested value automatically generated from title. Must be unique.')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('url', models.URLField(blank=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(help_text='80px X 80px', blank=True, upload_to='events')),
                ('image_alt_text', models.CharField(max_length=250, help_text='Describe the image as you would to someone over the phone. Max length 250 characters.')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['start_date', 'end_date', 'name'],
            },
        ),
    ]
