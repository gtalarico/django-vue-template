""" Production Settings """

import os
import dj_database_url
import environ

from .dev import *

env = environ.Env()

############
# DATABASE #
############
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}


############
# SECURITY #
############

DEBUG = env.bool('DJANGO_DEBUG', False)
# Set to your Domain here (eg. 'django-vue-template-demo.herokuapp.com')
ALLOWED_HOSTS = ['dj-v.herokuapp.com']
