import sys
import os

PROJECT_ROOT = os.path.dirname(__file__)

sys.path.insert(0, PROJECT_ROOT)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
