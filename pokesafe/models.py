"""Define the data model of the app."""

from django.db import models


class Pokemon(models.Model):
    """List the details of a given Pokemon."""

    name = models.CharField(max_length=200, unique=True)
    weight = models.IntegerField()

    def greet(self) -> str:
        """
        Make the Pokemon greet by saying who they are.

        Returns:
            str: Greeting.
        """
        return (
            f"Hi, my name is {self.name} and I weigh {self.weight}!"
            if self.weight is not None
            else f"Hi, my name is {self.name}!"
        )
