#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Griffin Calme'
SITENAME = "Griffin Calme's Blog on Programming in Science and Medicine"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Detroit'

DEFAULT_LANG = 'en'

THEME = "Theme"

# Navigation sections and relative URL:
SECTIONS = [('Blog', 'index.html'),
        ('Tags', 'tags.html'),
        ('Projects', 'pages/projects.html'),
        ('About', 'pages/about-me.html')]

GITHUB_URL = 'https://github.com/griffincalme'
TWITTER_USERNAME = 'griffincalme'



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/griffincalme'),
          ('Twitter', 'https://twitter.com/griffincalme'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
