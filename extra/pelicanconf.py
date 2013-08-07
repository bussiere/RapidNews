#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Bussiere'
SITENAME = u'Bussiere Rapid News'
SITEURL = 'http://bussiere.github.io/RapidNews'

TIMEZONE = 'Europe/Paris'
FEED_DOMAIN = 'http://bussiere.github.com/RapidNews'
DEFAULT_LANG = u'en'


# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),)
# Social widget
SOCIAL = (('Bussiere', 'https://github.com/bussiere'),)

DEFAULT_PAGINATION = 10

THEME = "../pelican-themes/simple2"
PLUGIN_PATH = "../pelican-plugins/"
PLUGINS = ['sitemap',]
FEED_MAX_ITEMS = 15
FEED_ATOM = 'feeds/all.atom.xml'
FEED_RSS = 'feeds/all.rss.xml'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}