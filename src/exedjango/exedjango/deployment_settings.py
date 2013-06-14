# Django settings for exedjango project.

from settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
       'default' : {
               'ENGINE' : 'django.db.backends.mysql',
               'NAME' : 'creyoco',
               'USER' : 'root',
               'PASSWORD' : 'ssl20qwerty',
               'HOST' : 'localhost',
               'PORT' : '',
       }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': '/home/dimitri/db/sqlite.db',                      # Or path to database file if using sqlite3.
#         'USER': '',                      # Not used with sqlite3.
#         'PASSWORD': '',                  # Not used with sqlite3.
#         'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#     }
# }

ALLOWED_HOSTS = ['129.187.81.136', '129.187.81.137']

SENDFILE_BACKEND = 'sendfile.backends.nginx'
SENDFILE_ROOT = MEDIA_ROOT
SENDFILE_URL = MEDIA_URL
