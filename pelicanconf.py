#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rachel Ehlers'
SITENAME = 'Rachel Ehlers'
SITEURL = 'https://rachelehlers.com'
OUTPUT_PATH = './output'
PATH = './content'

TIMEZONE = 'America/Boise'

DEFAULT_LANG = 'en'


THEME = '/Users/rachelehlers/pelican-themes/gum'


ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
STATIC_PATHS = ['images']


GITHUB_URL = 'https://github.com/rachelehlers11'
#TWITTER_URL = 'https://twitter.com/rachehlers'




'''
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)


# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/rachel-ehlers/'),
          ('Twitter', 'https://twitter.com/rachehlers'))
'''
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
#PLUGINS = ['ipynb.markup']
