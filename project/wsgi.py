"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

# This will set production as default, but we must still set it with an
# ENV on heroku to ensure that the migrate command runs agains the correct DB
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.prod')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
