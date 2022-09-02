"""Detail how to retrieve Pokemons."""
from pokesafe.api import get_pokemon_details, get_pokemon_urls
from pokesafe.models import Pokemon


def catch_pokemons() -> None:
    """Catch Pokemons from API and store them in database."""
    for url in get_pokemon_urls():
        print(f"> querying {url}")
        pokemon_details = get_pokemon_details(url)
        Pokemon.objects.update_or_create(**pokemon_details)


def clear_pokemons() -> None:
    """Clear previously caught Pokemons."""
    Pokemon.objects.all().delete()
