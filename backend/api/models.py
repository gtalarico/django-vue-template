from django.db import models
from rest_framework import serializers


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()

class Userprofile(models.Model):
    user_id = models.CharField(max_length=40, primary_key=True)   
    user_name = models.CharField(max_length=30, default="DATAHACK")
    email_address = models.CharField(max_length=200, default="")
    short_tax_rate = models.FloatField(default=0.0)
    long_tax_rate = models.FloatField(default=0.0)
    invest_horizon = models.FloatField(default=0.0)
    
class Stock(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name="stocks")
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    purchase_price = models.FloatField(default=-1.0)
    target_price = models.FloatField(default=0.0)
    expect_return_rate = models.FloatField(default=0.0)
    purchase_date = models.CharField(max_length=100)
    #purchase_date = models.DateTimeField("data purchase this stock.")


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')

