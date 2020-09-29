#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Eduardo Balbinot"
SITENAME = 'Eduardo Balbinot homepage'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

THEME = 'themes/Peli-Kiera'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'neighbors']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/balbinotdd'),
    ('linkedin', 'https://www.linkedin.com/in/eduardo-balbinot-astro'),
    ('github', 'https://github.com/balbinot'),
    ('facebook', 'https://facebook.com/eduardo.balbinot.77'),
)
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
