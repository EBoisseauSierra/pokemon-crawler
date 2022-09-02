"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from dj_static import Cling
from django.core.wsgi import get_wsgi_application

import pokesafe.pokemons as pokemons

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
port = int(os.environ.get("PORT", 8000))


# Initialize db
pokemons.clear_pokemons()  # Ensure we don't track legacy records
# pokemons.catch_pokemon()

application = Cling(get_wsgi_application())
