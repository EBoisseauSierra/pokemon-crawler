"""Configure app URLs.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pokesafe import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.pokemon_lists, name="pokemon_list"),
    path("populate_pokemon/", views.populate_pokemons, name="catch_them_all"),
    path("clear_pokemons/", views.drop_pokemons, name="release_them_all"),
    path("<str:pokemon_name>/", views.pokemon, name="pokemon_details"),
]
