"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from .api.views import index_view, MessageViewSet, AuthMessageViewSet

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)
router.register('authmessages', AuthMessageViewSet)

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),
    path('api/jwt-auth/', obtain_jwt_token),
    path('favicon.ico', favicon_view),
]


