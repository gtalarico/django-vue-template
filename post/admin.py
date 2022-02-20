from django.contrib import admin

from post.models import Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user','title','text')

admin.site.register(Message, MessageAdmin)