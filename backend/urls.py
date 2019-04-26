"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url

from rest_framework import routers

from .api.views import index_view, MessageViewSet, serve_worker_view

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

urlpatterns = [
    # http://localhost:8000/
    path('', index_view, name='index'),

    # serve static files for PWA
    path('index.html', index_view, name='index'),
    re_path(r'^(?P<worker_name>[\w-]+).json$', serve_worker_view, name='manifest'),
    re_path(r'^(?P<worker_name>[-\w\d.]+).js$', serve_worker_view, name='serve_worker'),
    re_path(r'^(?P<worker_name>[\w]+).txt$', serve_worker_view, name='robots'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/admin/
    path('admin/', admin.site.urls),
]