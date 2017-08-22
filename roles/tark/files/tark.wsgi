import os, sys, site

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
BASE_PATH = os.path.dirname(PROJECT_PATH)

os.environ['DJANGO_ENVIRONMENT'] = 'production'

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir(os.path.join(BASE_PATH, '/env/local/lib/python2.7/site-packages'))

sys.path.append(PROJECT_PATH)
sys.path.append(os.path.join(PROJECT_PATH, 'tark_rest'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'tark_rest.settings'
print BASE_PATH
# Activate your virtual env
activate_path = os.path.join(BASE_PATH, "env/bin/")
activate_env=os.path.join(activate_path, "activate_this" + "." + "py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
#application = django.core.handlers.wsgi.WSGIHandler()