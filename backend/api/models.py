from ast import Str
from django.conf import settings
from django.db import models
from django.conf import settings

class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


# class MessageSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Message
#         fields = ('url', 'subject', 'body', 'pk')
