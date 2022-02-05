"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""
# from os import name
from django.conf.urls import url, include
from django.contrib import admin
# from django.urls import path
from rest_framework import routers

from .api.views import index_view, MessageViewSet

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

urlpatterns = [

    # http://localhost:8000/
    # path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    # path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    url(r'^admin/', admin.site.urls),
    url(r'^api/post/', include('backend.api.post.urls')),
]
