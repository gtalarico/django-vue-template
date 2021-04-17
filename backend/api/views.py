from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets

import json
import datetime

from .models import Message, MessageSerializer


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


def get_profile(user_name):
    #include stock info
    default_profile = {
        "exist": 0, # 0 for not exist, 1 for exist.
        "user_name": user_name,
        "short_tax_rate": None,
        "long_tax_rate": None,
        "stocks":[], #Code of stocks
    }    
    
    # replace with DB request later. 
    with open('data.json', 'r') as f:
        all_profile = json.load(f)
    
    if user_name in all_profile.keys():
        return all_profile[user_name]
    else:
        return default_profile

def fecth_profile(request):
    assert request.cookies != None
    
    user_name = request.cookies.name
    
    user_profile = get_profile(user_name)
    if user_profile["exist"] == 0:
        return JsonResponse(user_profile) #No choiice, just renturn nothing.
    else:
        return JsonResponse(user_profile)
    
def set_profile(request):
    
