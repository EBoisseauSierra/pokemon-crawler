"""Detail how to retrieve Pokemons."""
from pokesafe.api import get_pokemon_details
from pokesafe.models import Pokemon


def catch_pokemon() -> None:
    """Catch Pokemons from API and store them in database."""
    for pokemon_to_catch in ["pokemon/3", "pokemon/2"]:
        pokemon_details = get_pokemon_details(pokemon_to_catch)
        Pokemon.objects.update_or_create(**pokemon_details)


def clear_pokemons() -> None:
    """Clear previously caught Pokemons."""
    Pokemon.objects.all().delete()
