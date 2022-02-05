from django.contrib import admin

from backend.api.models import Message
class MessageAdmin(admin.ModelAdmin):
    list_display=('user','title','text')

admin.site.register(Message, MessageAdmin)
