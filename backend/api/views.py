from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets


import yfinance as yf
from google.oauth2 import id_token
from google.auth.transport import requests
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

    user_profile = get_profile(user_name)

    return JsonResponse(user_profile)
    

def check_user():

    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        # Or, if multiple clients access the backend server:
        # idinfo = id_token.verify_oauth2_token(token, requests.Request())
        # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
        #     raise ValueError('Could not verify audience.')

        # If auth request is from a G Suite domain:
        # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
        #     raise ValueError('Wrong hosted domain.')

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        userid = idinfo['sub']
        redirect('set_profile')
    except ValueError:
        # Invalid token
        pass


def set_profile(request):
    if request.method == 'POST':
        data = request.body.decode("utf-8")
        json_data = json.loads(data)
        user_name = json_data.get("user_name")
    else:
        raise Exception()
    
    
    '''
    if request.method == 'POST':
        if request.FILES:
            myFile =None
            for i in request.FILES:
                myFile = request.FILES[i]
            if myFile:
                dir = os.path.join(os.path.join(BASE_DIR, 'static'),'profiles')
                destination = open(os.path.join(dir, myFile.name),'wb+')
                for chunk in myFile.chunks():
                    destination.write(chunk)
                destination.close()
    return HttpResponse('ok')
    '''


def get_stock_info(stock_code):
    msft = yf.Ticker(stock_code)
    # get stock info
    #print(msft.info)
    # get historical market data
    #hist = msft.history(period="5d")