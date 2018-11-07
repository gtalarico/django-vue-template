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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    #限速设置
    'DEFAULT_THROTTLE_CLASSES': (
            'rest_framework.throttling.AnonRateThrottle',   #未登陆用户
            'rest_framework.throttling.UserRateThrottle'    #登陆用户
        ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '3/minute',                   #每分钟可以请求两次
        'user': '5/minute'                    #每分钟可以请求五次
    }
}

import datetime
#有效期限
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),    #也可以设置seconds=20
    'JWT_AUTH_HEADER_PREFIX': 'JWT',                       #JWT跟前端保持一致，比如“token”这里设置成JWT
}

############
# SECURITY #
############

DEBUG = env.bool('DJANGO_DEBUG', False)
# Set to your Domain here (eg. 'django-vue-template-demo.herokuapp.com')
ALLOWED_HOSTS = ['.herokuapp.com']
