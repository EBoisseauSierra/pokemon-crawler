"""Utilities for interacting with the PokeAPI."""

import requests

from .models import Move

API_BASE_URL = "https://pokeapi.co/api/v2"
POKEMON_DETAILS_API = "pokemon"


def get_pokemon_details(pokemon_url: str) -> dict:
    """Return details of a Pokemon based on a Pokemon ID."""
    api_response = requests.get(pokemon_url).json()

    base_experience = api_response.get("base_experience")
    height = api_response.get("height")
    is_default = api_response.get("is_default")
    name = api_response.get("name")
    weight = api_response.get("weight")
    first_move, created = Move.objects.get_or_create(
        name=api_response.get("moves")[0].get("move").get("name")
    )

    return {
        "base_experience": base_experience,
        "height": int(height),
        "is_default": bool(is_default),
        "name": name,
        "weight": int(weight),
        "first_move": first_move,
    }


def get_pokemon_urls(batch_size=100, max_query=2) -> list[str]:
    """Retrieve the list of URLs for the Pokemons to catch."""
    query_count = 0
    pokemon_urls = []
    url_to_query = f"{API_BASE_URL}/{POKEMON_DETAILS_API}?limit={batch_size}"

    while url_to_query is not None and query_count < max_query:
        api_response = requests.get(url_to_query).json()
        pokemon_urls += get_urls_from_api_response(api_response)
        url_to_query = api_response.get("next")
        query_count += 1
    return pokemon_urls


def get_urls_from_api_response(api_response) -> list[str]:
    """Extract Pokemons' API URLs from batch API query."""
    urls = []
    for item in api_response["results"]:
        urls.append(item["url"])

    return urls
