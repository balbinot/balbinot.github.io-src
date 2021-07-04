#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Eduardo Balbinot"
SITENAME = 'Eduardo Balbinot'
SITEURL = ''
SITESUBTITLE = ''
PATH = 'content'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

THEME = 'themes/Peli-Kiera'

SATIC_PATHS=['images']

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'neighbors',  'advthumbnailer']
#'better_figures_and_images',
RESPONSIVE_IMAGES = True
FIGURE_NUMBERS = True


SUMMARY_MAX_LENGTH = 60
DEFAULT_PAGINATION = 10
#GITHUB_URL = 'https://github.com/' ## Add a github ribbon on top right for source code url

ARTICLE_EXCLUDES = ['templates'] ## ignore this directory for content
#TEMPLATE_PAGES = {
#    'templates/page.html': 'index.html',
#}

#INDEX_URL = '/index.html'
#INDEX_SAVEAS = 'pages/index.html'

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
    ('github', 'https://github.com/balbinot'),
    ('twitter', 'https://twitter.com/balbinotdd'),
    ('linkedin', 'https://www.linkedin.com/in/eduardo-balbinot-astro'),
    ('facebook', 'https://facebook.com/eduardo.balbinot.77'),
)
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
