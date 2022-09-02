"""Utilities for interacting with the PokeAPI."""

import requests

API_BASE_URL = "https://pokeapi.co/api/v2"


def get_pokemon_details(url_suffix: str) -> dict:
    """Return details of a Pokemon based on a API pointer."""
    url_to_query = f"{API_BASE_URL}/{url_suffix}"
    api_response = requests.get(url_to_query).json()

    name = api_response.get("name")
    weight = api_response.get("weight")

    return {"name": name, "weight": int(weight)}
