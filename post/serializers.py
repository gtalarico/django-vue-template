from post.models import Message
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'pk', 'user', 'title', 'text', 'timestamp'
        )
        read_only_fields = ['user']

    def validate_title(self, value):
        qs = Message.objects.filter(title__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if(qs.exists()):
            raise serializers.ValidationError("This is already created.")
        return value
