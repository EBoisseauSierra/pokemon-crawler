"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from dj_static import Cling
from django.core.wsgi import get_wsgi_application

from pokesafe.catch_pokemon import catch_pokemon

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
port = int(os.environ.get("PORT", 8000))


# initialize db by load a couple Pokemons
catch_pokemon()

application = Cling(get_wsgi_application())
