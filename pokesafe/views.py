"""Define the views of our data."""

import base64

from django.shortcuts import get_object_or_404, redirect, render, reverse

from .models import Pokemon
from .pokemons import catch_pokemons, clear_pokemons


def pokemon_lists(request):
    """Display detail of a Pokemon."""
    pokemons = Pokemon.objects.all()
    return render(
        request, "pokesafe/pokemon_list.html", {"pokemons": pokemons}
    )


def pokemon(request, pokemon_name):
    """Display detail of a Pokemon."""
    pokemon = get_object_or_404(Pokemon, name=pokemon_name)
    return render(request, "pokesafe/pokemon.html", {"pokemon": pokemon})


def populate_pokemons(request):
    """Catch all Pokemons and return to homepage."""
    if request.method == "POST":
        catch_pokemons()
    return redirect(reverse("pokemon_list"))


def drop_pokemons(request):
    """Catch all Pokemons and return to homepage."""
    if request.method == "POST":
        clear_pokemons()
    return redirect(reverse("pokemon_list"))


def egg(request):
    """Explain why CybSafe should hire me."""
    follow_me = (
        b"aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUSZ0PTQzcw=="
    )
    feeling_lucky = base64.b64decode(follow_me).decode("ascii")
    return render(request, "pokesafe/42.html", {"url": feeling_lucky})
