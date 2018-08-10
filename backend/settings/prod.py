""" Production Settings """

import os
import dj_database_url
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

DEBUG = False
# Set to your Domain here (eg. 'django-vue-template-demo.herokuapp.com')
ALLOWED_HOSTS = ['*']
