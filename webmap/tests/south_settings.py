# -*- coding: utf-8 -*-
"""
These settings are used by the ``manage.py`` command.

With normal tests we want to use the fastest possible way which is an
in-memory sqlite database but if you want to create South migrations you
need a persistant database.

Unfortunately there seems to be an issue with either South or syncdb so that
defining two routers ("default" and "south") does not work.

"""
from .test_settings import *  # NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'webmap-corpus',
        'USER': 'webmap',
        'PASSWORD': 'webmap',
        'HOST': 'localhost',
        'PORT': '',
    },
}

INSTALLED_APPS.append('south', )
INSTALLED_APPS.append('author', )
INSTALLED_APPS.append('django.contrib.gis', )
INSTALLED_APPS.append('constance', )
INSTALLED_APPS.append('positions', )
INSTALLED_APPS.append('constance.backends.database', )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'author.middlewares.AuthorDefaultBackendMiddleware',
)

USE_I18N = True
USE_L10N = True

LANGUAGE_CODE = 'cs_CZ'

CONSTANCE_APP_NAME = "webmap"
CONSTANCE_CONFIG = {
    'MAP_BASELON': (14.4211, u'zeměpisná délka základní polohy mapy'),
    'MAP_BASELAT': (50.08741, u'zeměpisná délka základní polohy mapy'),
    'MAP_BOUNDS': ("14.22, 49.95, 14.8, 50.18", u'hranice zobrazení mapy'),
}
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
