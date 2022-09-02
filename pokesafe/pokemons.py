"""Detail how to retrieve Pokemons."""
from pokesafe.api import get_pokemon_details
from pokesafe.models import Pokemon


def catch_pokemons() -> None:
    """Catch Pokemons from API and store them in database."""
    for pokemon_id in _get_list_of_pokemon_ids():
        pokemon_details = get_pokemon_details(pokemon_id)
        Pokemon.objects.update_or_create(**pokemon_details)


def clear_pokemons() -> None:
    """Clear previously caught Pokemons."""
    Pokemon.objects.all().delete()


def _get_list_of_pokemon_ids() -> list[str]:
    """Retrieve the list of IDs for the Pokemons to catch."""
    return [2, 3]
