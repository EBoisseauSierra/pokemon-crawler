"""Detail app config."""


from django.apps import AppConfig


class PokesafeConfig(AppConfig):
    """Config of our PokeSafe app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "pokesafe"
