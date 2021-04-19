from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required

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
        "stocks":{
            'APPL':{
                
            }
        }, #Code of stocks
    }    
    # replace with DB request later. 
    try:
        with open('data.json', 'r') as f:
            all_profile = json.load(f)
    except:
        return default_profile
    
    if user_name in all_profile.keys():
        return all_profile[user_name]
    else:
        return default_profile
    
@login_required(login_url='')
def fecth_profile(request):
    user_name = request.user["email"]
    # have get user_name

    user_profile = get_profile(user_name)

    return JsonResponse(user_profile)
    

def check_user(request):
    #保存session的值到服务器
    request.session['KEY'] = VALUE
    #获取session的值
    VALUE = request.session['KEY']
    VALUE = request.session.get('KEY', 缺省值)
    del request.session['KEY']
    request.session.flush()#删除所有session

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


def set_profile_storage(user_name, user_profile):
    #repalce with DB later
    try:
        with open('data.json', 'wr') as f:
            all_profile = json.load(f)
            all_profile[user_name] = user_profile
            json.dump(all_profile, f)
    except:
        with open('data.json', 'w') as f:
            all_profile = {}
            all_profile[user_name] = user_profile
            json.dump(all_profile, f)
    return user_profile

@login_required(login_url='')
def set_profile(request):
    user_name = request.user['email']
    if request.method == 'POST':
        data = request.body.decode("utf-8")
        json_data = json.loads(data)
        user_name = json_data.get("user_name")
    else:
        raise Exception()
    
    previous_profile = get_profile(user_name)
    
    previous_profile["exist"] = 1
    previous_profile["user_name"] = user_name
    previous_profile["short_tax_rate"] = json_data.get("short_tax_rate")
    previous_profile["long_tax_rate"] = json_data.get("long_tax_rate")
    #previous_stock_list = previous_profile["stocks"].keys()
    
    for stock_k in json_data.get("stocks").keys():
        previous_profile["stocks"][stock_k] = json_data.get("stocks")[stock_k] 
    
    set_profile_storage(user_name, previous_profile)
    
    return JsonResponse(previous_profile)
    
    
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


def get_stock_info(stock_code_list):
    """
        There’re some limitations by making the call to Yahoo Finance API:
            Using the Public API (without authentication), you are limited to 2,000 requests per hour per IP (or up to a total of 48,000 requests a day).
            I’m not sure it’s precisely for Financial data. But please use time.sleep(1) to avoid your IP getting blocked.
    """
    detail_info = {}
    for code in stock_code_list:
        sotck = yf.Ticker(code)
        try:
            close_price = sotck.history(period='1d')["Close"][0]
            stock_name = sotck.info['longName']
            current_date = datetime.datetime.now()
        except:
            raise Exception("No such stock in the market.")
        
        detail_info[code] = {
            'close': close_price,
            'name': stock_name,
            'current_date': current_date
        }
    
    return detail_info
        
    #print(msft.info)
    # get historical market data
    #hist = msft.history(period="5d")

def get_held_stock(user_name):
    try:
        with open('data.json', 'r') as f:
            all_profile = json.load(f)
            if user_name in all_profile.keys():
                return all_profile[user_name]['stocks']
            else:
                raise Exception("No user")
    except:
        raise Exception("Fail to get stock info")

@login_required(login_url='')
def stock_detail(request):
    '''
        expect to recevie a json:
            {
                "user_name": 'NAME
                "stocks": [
                    'APPL',
                    'NIO',
                ]
            }
    '''
    #return blank dict
    if request.method == '':
        data = request.body.decode("utf-8")
        json_data = json.loads(data)
        user_name = json_data.get("user_name")
        stock_list = json_data.get("stocks")
    else:
        raise Exception()
    
    current_stock_info = get_sotck_info(stock_list)
    held_stock_info = get_held_stock(user_name)
    
    stock_info = {}
    for stock in stock_list:
        stock_info[stock] = dict(held_stock_info[stock], **current_stock_info[stock]) 
    
    return JsonResponse(sotck_info)
    