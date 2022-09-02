"""Utilities for interacting with the PokeAPI."""

import requests

API_BASE_URL = "https://pokeapi.co/api/v2"
POKEMON_DETAILS_API = "pokemon"


def get_pokemon_details(pokemon_id: str) -> dict:
    """Return details of a Pokemon based on a Pokemon ID."""
    url_to_query = f"{API_BASE_URL}/{POKEMON_DETAILS_API}/{pokemon_id}"
    api_response = requests.get(url_to_query).json()

    name = api_response.get("name")
    weight = api_response.get("weight")

    return {"name": name, "weight": int(weight)}
