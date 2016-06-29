# -*- encoding: utf-8 -*-
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'temp.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'connexionsw_testing',
#        'USER': 'postgres',
#        'PASSWORD': '',
#        'HOST': '',
#        'PORT': '',
#    }
#}
