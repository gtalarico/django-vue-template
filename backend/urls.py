"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .api.views import index_view, MessageViewSet, get_profile, set_profile, stock_detail, google_login, google_logout, add_new_stock, delete_stock, stock_detail

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),
    
    path('login/', google_login),
    
    path('logout/', google_logout),
    
    path('profile/set/', set_profile),
    
    path('profile/add_stock/', add_new_stock),
    
    path('profile/set_stock/', set_stock),
    
    path('profile/delete/', delete_stock),
    
    path('profile/stock_detail/', stock_detail), #id, s_code
    
    #path('/profile/<int:u_id>', get_profile),
    path('profile/', get_profile)
]


