#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic settings of the website
AUTHOR = 'Miroslav Gasparek'
SITENAME = 'Miroslav Gasparek'
SITEURL = 'https://www.miroslavgasparek.com'

# Hide the site name
HIDE_SITENAME = True

# Add the site logo and set the logo size
SITEURL = ''
SITELOGO = 'images/favicon_bioeng.jpg'
SITELOGO_SIZE = 28

# Select the output path
PATH = 'content'

# Add timezone
TIMEZONE = 'Europe/Paris'

# Select default language
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

PAGE_PATHS = ['pages']  
# PAGE_URL = 'pages/{slug}.html'
# PAGE_SAVE_AS = 'pages/{slug}.html'


# Set menu items
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('About', '/pages/about.html'),
    ('Blog', '/category/blog.html'),
    ('Projects','/pages/projects.html'),
    ('CV', '/pdf/cv_mg_academic.pdf'),
    ('Media', '/pages/media.html'),
    ('Contact', '/pages/contact.html')
    )

# Blogroll
LINKS = (('Podcast </br>"Pravidelná Dávka" ', 'https://pravidelnadavka.sk'),
         )

# Social widget
SOCIAL = (
      ('LinkedIn', 'https://www.linkedin.com/in/miroslavgasparek/'),
          ('Twitter', 'https://twitter.com/MiroGasparek'),
          ('Github', 'https://github.com/miroslavgasparek'),
          ('Instagram', 'https://www.instagram.com/miroslav_gasparek/?hl=en'))

# Number of blogposts per page
DEFAULT_PAGINATION = 10

# Add static paths 
STATIC_PATHS = ['images',
        'pages',
        'extra/CNAME', 'extra/robots.txt','extra/custom.css','pdf']

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/robots.txt': {'path': 'robots.txt'},
                       'extra/custom.css': {'path': 'static/custom.css'}
                       }

# Add the custon CSS
CUSTOM_CSS = 'static/custom.css'

# Select the theme and add the JINJA environment
THEME = 'pelican-themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Add the plugins as needed
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites','liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook','ipynb.markup']


# Set the mark-ups
MARKUP = ('md','ipynb')

# Ignore files as needed
IGNORE_FILES = [".ipynb_checkpoints"]  

# Do not load the content cache
LOAD_CONTENT_CACHE = False

# Delete output directory
DELETE_OUTPUT_DIRECTORY = False


# Use the metadata in the notebook
IPYNB_USE_METACELL = True


# Set About Me sidebar 
SHOW_ABOUTME = True
AVATAR = 'images/avatar_pic.jpg'
BANNER = 'images/background_pic.svg'
FAVICON = 'images/favicon_bioeng.jpg'
ABOUT_ME = """
I like to think about how <br>
mathematics, computing, <br>
and engineering principles <br>
can be applied to biological <br>
systems to solve the major <br>
global healthcare, economic <br>
and environmental issues <br> 
and to advance our <br>
understanding of biology. <br> <br>

I am fascinated by synthetic biology,
systems biology,  <br>
building artificial cells, <br> 
genetic circuits design, <br> control
theory, and machine learning. <br><br>

I also like asking questions, <br>
especially "Why?" and "Why does it matter?",
meaningful disputes, lifting weights, <br>
science popularization, <br>
and good coffee.
"""

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True