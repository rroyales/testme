import os
import sys
 
path = '/srv/www/hello/hello'
if path not in sys.path:
    sys.path.insert(0, '/srv/www/hello/hello')
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'hello.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
