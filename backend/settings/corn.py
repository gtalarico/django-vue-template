from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .models import Message, MessageSerializer
from .models import Userprofile, Stock

from django.shortcuts import *
from .models import UserProfile
from .views import compute_D
from .forms import ProfileForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def my_task():
    '''
    access to all User information and print all User's id and email address
    '''
    all_user = Userprofile.objects.all()
    for user in all_user:
        print(user.user_id, ' : ', user.email_address)
        if user.sell_notify > 0:
            opp_r = user.opportunity_cost
            tax_s = user.short_tax_rate
            tax_l = user.long_tax_rate  # by dafault.
            full_horizon = user.invest_horizon
            #send_email
            for s in user.stocks.all():
                s_code = s.code
                yf_stock = yf.Ticker(s_code)
                purchase_date = s.purchase_date
                p0 = s.purchase_price 
                pl = s.target_price
                ps = yf_stock.history(period='1d')["Close"][0]
                hs = ((timezone.now() - purchase_date).days) / 365     # in year
                left_horizon = full_horizon - hs if (full_horizon - hs) > 0 else 0
                close_date = yf_stock.history(period='1d').index[0].isoformat()[:10]
                D = compute_D(tax_l, tax_s, pl, ps, p0, opp_r, left_horizon, hs)
                if D < 0:
                    if s._sended < 1.:
                        send_mail('SELL NOTIFICATION',
                                  f'Time to sell {s.name}',
                                  settings.EMAIL_HOST_USER,
                                  [user.email, 'qf31@tamu.edu'],
                                  fail_silently=False,)
                    s._sended = 1.0 # sended now
                else:
                    s._sended = 0.0  
                s.save()
        else:
            pass # No action