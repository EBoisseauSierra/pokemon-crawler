"""Define the data model of the app."""

from django.db import models


class Pokemon(models.Model):
    """List the details of a given Pokemon."""

    name = models.CharField(max_length=200)
    weight = models.IntegerField()
