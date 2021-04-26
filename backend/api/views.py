from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.utils import timezone

import yfinance as yf
from google.oauth2 import id_token
from google.auth.transport import requests as grequests
import json
from datetime import datetime as pydate
import datetime

from .models import Message, MessageSerializer
# from .models import Userprofile, Stock
import importlib

backend_models = importlib.import_module(".models", package="backend.api")
Userprofile = backend_models.Userprofile


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html')) # pragma: no cover


def import_test_models():
    global Userprofile
    backend_test_models = importlib.import_module(".test_models", package="backend.api")
    Userprofile = backend_test_models.Userprofile
    # print(Userprofile)


class MessageViewSet(viewsets.ModelViewSet): # pragma: no cover
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


def get_profile(request):
    #include stock info
    try:
        data = request.body.decode("utf-8")
        json_data = json.loads(data)
        u_id = json_data.get("id")
        user = Userprofile.objects.get(user_id=u_id)
        stocks = {}
        for s in user.stocks.all():
            close_price =  yf.Ticker(s.code).history(period='1d')["Close"][0]
            stocks[s.code] = {
                "code": s.code,
                "close_price": close_price,
                "purchase_price": s.purchase_price,
                "purchase_date": s.purchase_date.isoformat()[:10],
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
    except Exception as e:
        print(e)
        return HttpResponse("Get user failed!")


def set_profile(request):
    try:
        if request.method == 'POST':
            data = request.body.decode("utf-8")
            json_data = json.loads(data)
        else:
            raise Exception()
        
        u_id = json_data.get("id")
        user = Userprofile.objects.get(user_id=u_id)
        user.short_tax_rate = json_data.get("short_tax_rate")
        user.long_tax_rate = json_data.get("long_tax_rate")
        user.invest_horizon = json_data.get("investment_horizon")
        
        
        '''
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
        '''
        stocks = {}
        user_profile = {
            "state": 'success',
            "user_id": u_id,
            "user_name": user.user_name,
            "short_tax_rate": user.short_tax_rate,
            "long_tax_rate": user.long_tax_rate,
            "investment_horizon": user.invest_horizon,
            "stocks": stocks
        }
        user.save()
        return JsonResponse(user_profile)
    except:
        return HttpResponse("Set failed!")


def compute_return(ts, tl, p0, pl, ps, r): # pragma: no cover
    # wait    
    return 2.0

    

def stock_detail(request): # pragma: no cover
    
    def compute_short_return():    
        #wait
        return 0.0
    
    def compute_long_return():
        #wait
        return 0.0
    
    data = request.body.decode("utf-8")
    json_data = json.loads(data)
    
    u_id = json_data.get("id")
    s_code = json_data.get("s_code")
    user = Userprofile.objects.get(user_id=u_id)
    stock = user.stocks.get(code=s_code)
    yf_stock = yf.Ticker(s_code)

    # import pdb
    # pdb.set_trace()

    purchase_date = stock.purchase_date
    full_horizon = user.invest_horizon
    p0 = stock.purchase_price 
    pl = stock.target_price
    ps = yf_stock.history(period='1d')["Close"][0]
    hs = ((timezone.now() - purchase_date).days) / 365     # in year
    r = 0.001 # 基准利率？
    left_horizon = full_horizon - hs
    a_s = compute_short_return()
    a_l = compute_long_return()
    # wait...
    
    close_date = yf_stock.history(period='1d').index[0].isoformat()[:10]
    stock_info = {
        "stock_code": s_code,
        "stock_name": stock.name,
        "purchase_price": p0,
        "purchase_date": purchase_date.isoformat()[:10],
        "target_price": pl,
        "expect_return_rate": stock.expect_return_rate,
        "close_price": ps,
        "close_date": close_date,
        "horizon": hs,
        "opportunity_cost": r,
        "left_horizon": left_horizon,
        "short_return": a_s,
        "long_return": a_l,
    }
    return JsonResponse(stock_info)

def delete_stock(request):
    try:
        if request.method == 'POST':
            data = request.body.decode("utf-8")
            json_data = json.loads(data)
        else:
            raise Exception()
        
        u_id = json_data.get("id")
        user = Userprofile.objects.get(user_id=u_id)
        delete_list = json_data.get("deleted_stocks")
        for code in delete_list:
            user.stocks.get(code=code).delete()
            
        return HttpResponse("Deleting Succeeded!")
    except:
        return HttpResponse("Deleting failed!")

def set_stock(request):
    try:
        if request.method == 'POST':
            data = request.body.decode("utf-8")
            json_data = json.loads(data)
        else:
            raise Exception()
            
        u_id = json_data.get("id")
        s_code = json_data.get("s_code")
        user = Userprofile.objects.get(user_id=u_id)
        modified_stock = user.stocks.get(code=s_code)
        modified_stock.purchase_date = datetime.date.fromisoformat(json_data.get("purchase_date")[:10])
        modified_stock.purchase_price = json_data.get("purchase_price")
        modified_stock.target_price = json_data.get("target_price")
        modified_stock.expect_return_rate = json_data.get("expect_return_rate")
        modified_stock.save()
        
        return HttpResponse("Setting Stock Succeeded!")
    except:
        return HttpResponse("Setting Stock failed!")
    
def add_new_stock(request): # pragma: no cover
    try:        
        if request.method == 'POST':
            data = request.body.decode("utf-8")
            json_data = json.loads(data)
        
        u_id = json_data.get("id")
        user = Userprofile.objects.get(user_id=u_id)
        for k,v in json_data.get("added_stocks").items():
            user.stocks.create( code=k,
                                name=yf.Ticker(k).info["longName"],
                                purchase_price=v["purchase_price"],
                                purchase_date=datetime.date.fromisoformat(v["purchase_date"][:10]),
                                target_price=v["target_price"],   # may fail for the format as str.
                                expect_return_rate=v["expect_return_rate"])
        
        return HttpResponse("Adding Succeeded!")
    except Exception as e:
        return HttpResponse("Adding failed!")


def google_login(request): # pragma: no cover
    if request.method == "POST":
        try:
            raw_data = request.body.decode("utf-8") # assume: send by json 
            json_data = json.loads(raw_data)
            token = json_data.get('id_token')
            #token = json_data.get("access_token")
            # token = request.data.get("id_token")
            # # Specify the CLIENT_ID of the app that accesses the backend:
            idinfo = id_token.verify_oauth2_token(token, grequests.Request(), "1052465622185-hl3qvsb6o5j432c95bb9fritksuuq4vh.apps.googleusercontent.com")
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
                                       user_name=idinfo["name"])
                new_user.save()

            request.session['user_id'] = user_id
            request.session['is_login'] = True
            request.session.set_expiry(20*60) # 20 minutes
            # state
            return JsonResponse({"user_id": user_id,
                                 "state": True})
        except ValueError:
            # Invalid token
            # 失败原因，state。
            return JsonResponse({"state": False}, )
            pass

def google_logout(request): # pragma: no cover
    try:
        request.session.flush()
        return HttpResponse("You're logged out.")
    except KeyError:
        return HttpResponse("Logging out failed.")
    