from django.db import models
from rest_framework import serializers

class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')

class AuthMessage(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    nick_name = models.CharField('昵称',max_length=50,default='Secret')


class AuthMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuthMessage
        fields = ('url', 'subject', 'body', 'nick_name', 'pk')
