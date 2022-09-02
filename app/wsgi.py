"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from dj_static import Cling
from django.core.wsgi import get_wsgi_application

from pokesafe.api import get_pokemon_details
from pokesafe.models import Pokemon

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
port = int(os.environ.get("PORT", 8000))


# initialize db by load a couple Pokemons
for pokemon_to_catch in ["pokemon/3", "pokemon/2"]:
    pokemon_details = get_pokemon_details(pokemon_to_catch)
    Pokemon(**pokemon_details).save()

application = Cling(get_wsgi_application())
