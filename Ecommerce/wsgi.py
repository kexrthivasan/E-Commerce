"""
WSGI config for Ecommerce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'Ecommerce.deployment' if 'WEBSITE_HOSTNAME' os.environ else 'Ecommerce.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings_module')

application = get_wsgi_application()
