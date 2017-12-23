#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rachel Ehlers'
SITENAME = 'Rachel Ehlers'
SITEURL = ''

PATH = './content'

TIMEZONE = 'America/Boise'

DEFAULT_LANG = 'en'


THEME = '/Users/rachelehlers/pelican-themes/gum'
#THEME = "notmyidea"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



#GITHUB_URL = 'https://github.com/rachelehlers11'
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

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
