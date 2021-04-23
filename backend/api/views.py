from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required

import yfinance as yf
from google.oauth2 import id_token
from google.auth.transport import grequests
import json
import datetime

from .models import Message, MessageSerializer, Userprofile, Stock


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


def get_profile(request):
    #include stock info
    u_id = request.GET.get("id")
    try:
        user = Userprofile.objects.get(user_id=u_id)
        stocks = {}
        for s in user.stocks:
            close_price =  yf.Ticker(s.code).history(period='1d')["Close"][0]
            stocks[s.code] = {
                "code": s.code,
                "close_price": close_price,
                "purchase_price": s.purchase_price,
                "purchase_date": s.purchase_date,
                "target_price": s.target_price,
                "expect_return_rate": s.expect_return_rate 
            }
        
        user_profile = {
            "user_id": u_id,
            "user_name": user.user_name,
            "short_tax_rate": user.short_tax_rate,
            "long_tax_rate": user.long_tax_rate,
            "investment_horizon": user.invest_horizon,
            "stocks": stocks
        }
        return JsonResponse(user_profile)
    except:
        return HttpResponse("Get user failed!")



def set_profile(request):
    try:
        u_id = request.GET.get("id")
        user = Userprofile.objects.get(user_id=u_id)

        if request.method == 'POST':
            data = request.body.decode("utf-8")
            json_data = json.loads(data)
        else:
            raise Exception()
        
        user.short_tax_rate = json_data.get("short_tax_rate")
        user.long_tax_rate = json_data.get("long_tax_rate")
        user.invest_horizon = json_data.get("investment_horizon")
        
        stocks = json_data.get("stocks")
        # require all stocks haven't been in DB.
        for k, v in stocks.items():
            stock_code = k
            stock_info = yf.Ticker(s.code)
            close_price = stock_info.history(period='1d')["Close"][0]
            stock_name = stock_info.info['longName']
            _stock = user.stocks.create(code=k, 
                                        name=stock_name,
                                        purchase_price=v["purchase_price"],
                                        purchase_date=v["purchase_date"],
                                        target_price=v["target_price"],
                                        expect_return_rate=v["expect_return_rate"])
            stocks[k]["code"] = k
            stocks[k]["close_price"] = close_price
        
        user_profile = {
            "user_id": u_id,
            "user_name": user.user_name,
            "short_tax_rate": user.short_tax_rate,
            "long_tax_rate": user.long_tax_rate,
            "investment_horizon": user.invest_horizon,
            "stocks": stocks
        }
        
        return JsonResponse(previous_profile)
    except:
        return HttpResponse("Set failed!")



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



def stock_detail(request):
    #return blank dict
    u_id = request.GET.get("id")
    s_code = request.GET.get("s_code") # 也可以从json中？   
    
    user = Userprofile.objects.get(user_id=u_id)
    stock = user.stocks.get(code=s_code)
    yf_stock = yf.Ticker(s_code)
    
    close_price = yf_stock.history(period='1d')["Close"][0]
    
    
    stock_info = {}

    
    return JsonResponse(sotck_info)

def delete_stock(request):
    try:
        u_id = request.GET.get("id")
        user = Userprofile.objects.get(user_id=u_id)
        
        if request.method == 'POST':
            data = request.body.decode("utf-8")
            json_data = json.loads(data)
        else:
            raise Exception()
        
        delete_list = json_data.get("deleted_stocks")
        for code in delete_list:
            user.stocks.get(code=code).delete()
            
        return HttpResponse("Deleting Succeeded!")
    except:
        return HttpResponse("Deleting failed!")

def add_new_stock(request):
    try:
        u_id = request.GET.get("id")
        user = Userprofile.objects.get(user_id=u_id)
        
        if request.method == 'POST':
            data = request.body.decode("utf-8")
            json_data = json.loads(data)
        else:
            raise Exception()
        
        for k,v in json_data.get("added_stocks").items():
            user.stocks.create( code=k,
                                name=yf.Ticker(k).info["longName"],
                                purchase_price=v["purchase_price"],
                                purchase_date=v["purchase_date"],
                                target_price=v["target_price"],   # may fail for the format as str.
                                expect_return_rate=v["expect_return_rate"])
        
        return HttpResponse("Adding Succeeded!")
        
    except:
        return HttpResponse("Adding failed!")


def google_login(request): 
    if request.method == "POST":
        try:
            #raw_data = request.body.decode("utf-8") # assume: send by json 
            #json_data = json.loads(raw_data)
            #token = json_data.get("access_token")
            token = request.data.get("id_token")
            # Specify the CLIENT_ID of the app that accesses the backend:
            idinfo = id_token.verify_oauth2_token(token, grequests.Request(), "MY CLIENT ID")
            user_id = idinfo['sub']
            '''
                {
                // These six fields are included in all Google ID Tokens.
                "iss": "https://accounts.google.com",
                "sub": "110169484474386276334",
                "azp": "1008719970978-hb24n2dstb40o45d4feuo2ukqmcc6381.apps.googleusercontent.com",
                "aud": "1008719970978-hb24n2dstb40o45d4feuo2ukqmcc6381.apps.googleusercontent.com",
                "iat": "1433978353",
                "exp": "1433981953",

                // These seven fields are only included when the user has granted the "profile" and
                // "email" OAuth scopes to the application.
                "email": "testuser@gmail.com",
                "email_verified": "true",
                "name" : "Test User",
                "picture": "https://lh4.googleusercontent.com/-kYgzyAWpZzJ/ABCDEFGHI/AAAJKLMNOP/tIXL9Ir44LE/s99-c/photo.jpg",
                "given_name": "Test",
                "family_name": "User",
                "locale": "en"
                }
            '''
            try:
                Userprofile.objects.get(user_id=user_id)
            
            except:
                new_user = Userprofile(user_id=user_id, 
                                       email_address=idinfo["email"], 
                                       name=idinfo["name"])
                new_user.save()

            request.session['user_id'] = user_id
            request.session['is_login'] = True
            request.session.set_expiry(20*60) # 20 minutes
            return JsonResponse({"user_id": user_id})
        except ValueError:
            # Invalid token
            return HttpResponse("Login failed. Invalid access token.")
            pass

def google_logout(request):
    try:
        request.session.flush()
        return HttpResponse("You're logged out.")
    except KeyError:
        return HttpResponse("Logging out failed.")
    