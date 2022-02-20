# Create your views here.
from django.db.models import Q
from post.permissions import IsOwnerOrReadOnly
from post.serializers import PostSerializer
from rest_framework import generics,mixins
from post.models import Message
from .serializers import PostSerializer

class PostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = Message.objects.all()
        query = self.request.GET.get('q') #'q' is search text. e.g /?q=hello
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)|Q(text__icontains=query)).distinct() #search part
        return qs
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) #user authentication for create
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Message.objects.all()