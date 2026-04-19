import os
from django.core.wsgi import get_wsgi_application

# Make sure this matches your folder name!
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autovision_core.settings")

application = get_wsgi_application()