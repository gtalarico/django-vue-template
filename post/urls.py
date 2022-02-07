from django.conf.urls import url
from .views import PostAPIView, PostRudView

urlpatterns = [
    url(r'^$', PostAPIView.as_view(), name='post-api'),
    url(r'^(?P<pk>\d+)/$', PostRudView.as_view(), name='post-rud'),  
]  