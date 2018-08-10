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
# Set to your Domain
ALLOWED_HOSTS = ['django-vue-template-demo.herokuapp.com']


##########
# STATIC #
##########

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
WHITENOISE_ROOT = STATICFILES_DIRS[0]
# Set but not used
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Insert Whitenoise Middleware at top but below Security Middleware
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware',)
# http://whitenoise.evans.io/en/stable/django.html#make-sure-staticfiles-is-configured-correctly

