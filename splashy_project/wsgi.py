"""
WSGI config for splashy_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
# coding=utf-8
from __future__ import unicode_literals

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "splashy_project.settings")

# Original:
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

# From Heroku's Getting Started With Django page:
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application()) 

# From Heroku's Django Assets page:
# from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise

# application = get_wsgi_application()
# application = DjangoWhiteNoise(application)