from django.db.models import Q
from backend.api.post.permissions import IsOwnerOrReadOnly
from backend.api.post.serializers import PostSerializer
from rest_framework import generics,mixins
from backend.api.models import Message
from .serializers import PostSerializer

class PostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = Message.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)|Q(text__icontains=query)).distinct()
        return qs
    def perform_create(self, serialzer):
        serialzer.save(user=self.request.user)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Message.objects.all()