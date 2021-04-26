""" Production Settings """

import os
import dj_database_url
import django_heroku

from .dev import *

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

DEBUG = bool(os.getenv('DJANGO_DEBUG', ''))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)


# Set to your Domain here (eg. 'django-vue-template-demo.herokuapp.com')
ALLOWED_HOSTS = ['portfoliotradingassistant.herokuapp.com', 'localhost:8000', 'localhost:8080']

django_heroku.settings(locals())
