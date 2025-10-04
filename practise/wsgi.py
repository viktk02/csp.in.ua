import os
import sys
from django.core.wsgi import get_wsgi_application
#different from production
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practise.settings')

application = get_wsgi_application()
