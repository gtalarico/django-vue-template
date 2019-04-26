from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.conf import settings

from rest_framework import viewsets
import os

from .models import Message, MessageSerializer


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))
# pwa_view = never_cache(TemplateView.as_view(template_name='manifest.json'))

def serve_worker_view(request, worker_name):
	"""
	Serve the requested service worker from the appropriate location in the static files.
	We need to serve the worker this way in order to allow it access to requests made against the
	root - whatever /sub/dir the worker ends up getting served from is the only location it will
	have visibility on, so serving from / is the only way to ensure the worker has visibility on all
	requests. Only a-zA-Z-_ characters can appear in the service worker name.

	:param request:
	:param worker_name:
	:return:
	"""
	if worker_name == 'manifest':
		worker_path = os.path.join(settings.STATIC_ROOT, f"{worker_name}.json")
	elif worker_name == 'robots':
		worker_path = os.path.join(settings.STATIC_ROOT, f"{worker_name}.txt")
	else:
		worker_path = os.path.join(settings.STATIC_ROOT, f"{worker_name}.js")
	try:
		with open(worker_path, 'r') as worker_file:
			return HttpResponse(worker_file, content_type='application/javascript')
	except IOError:
		return HttpResponseNotFound('serviceWorkers not found!')


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
