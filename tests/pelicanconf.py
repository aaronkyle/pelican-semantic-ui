#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = 'Test'
SITENAME = 'Test Blog'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = 'tw'

# LOCALE = ('zh-TW', 'en_US')

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PATH = 'content'
THEME = "../"

DEFAULT_PAGINATION = 10


# Menu

DISPLAY_CATEGORIES_ON_MENU = True


# Pages

PAGE_PATHS = ['pages']
PAGE_EXCLUDES = []

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)


