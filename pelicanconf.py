#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hector T.'
SITENAME = 'Blog De Hector'
SITEURL = 'https://hectorfranc.github.io/blog-de-hector'
# SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS=['sitemap']

SITEMAP = {
    'format': 'xml',
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'weekly',
        'pages': 'monthly',
    },
    'priorities': {
        'articles': 0.9,
        'indexes': 0.7,
        'pages': 0.5,
    },
    'exclude': ['tags', 'categories', 'author', 'archives'],
}

# Page urls
ARTICLE_URL = '{slug}'
DRAFT_URL = 'drafts/{slug}'
PAGE_URL = 'pages/{slug}'
DRAFT_PAGE_URL = 'drafts/pages/{slug}'
AUTHOR_URL = 'author/{slug}'
CATEGORY_URL = 'category/{slug}'
TAG_URL = 'tag/{slug}'

DEFAULT_CATEGORY = 'todos'

# Themes
THEME = 'themes/hector-theme'
