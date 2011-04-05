# -*- coding: utf-8 -*-

from local_settings import *


DEFAULT_CHARSET = 'utf-8'

EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = '[MutluGünümüz] '
DEFAULT_FROM_EMAIL = 'info@mutlugunumuz.com'

ADMINS = (('onur mat', 'omat@gezgin.com'),)
MANAGERS = ADMINS

TIME_ZONE = 'Europe/Istanbul'

LANGUAGE_CODE = 'tr'

SITE_ID = 1

USE_I18N = True

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'z7xc&y*3--xh-8ryer34*)ay_6ciqdhm#^7+y#3ibosnvpxgmd'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.formtools',
    'event',
    'comments',
    'thumbnail',
    'tagging',
    'registration',
)

TEMPLATE_CONTEXT_PROCESSORS = ("django.core.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
#                               "django.core.context_processors.media",
                               "django.core.context_processors.request",)

INTERNAL_IPS = ('127.0.0.1',)

AUTH_PROFILE_MODULE = 'userprofiles.UserProfile'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

CACHE_KEY_PREFIX = 'mutlugunumuz'

