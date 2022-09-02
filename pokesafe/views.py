"""Define the views of our data."""

from django.shortcuts import get_object_or_404, render

from .models import Pokemon


def pokemon(request, pokemon_name):
    """Display detail of a Pokemon."""
    pokemon = get_object_or_404(Pokemon, name=pokemon_name)
    return render(request, "pokesafe/pokemon.html", {"pokemon": pokemon})
