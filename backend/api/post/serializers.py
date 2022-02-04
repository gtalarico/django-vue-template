from backend.api.models import Message
from rest_framework import serializers
from backend.api.models import Message

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'pk', 'user', 'title', 'text', 'timestamp'
        ]
        read_only_fields = ['user']

    def validate_title(self, value):
        qs = Message.objects.filter(title__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.exclude.pk)
        if(qs.exists()):
            return serializers.ValidationError("This is already created.")
        return value
