#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = 'Jason'
SITENAME = 'Pelican Semantic Demo'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PATH = 'content'
THEME = "../"

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['plugins']
PLUGINS = ["pelican-go-semantic-ui"]

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
