"""Define the data model of the app."""

from django.db import models


class Move(models.Model):
    """Represent a given 'move' of a Pokemon."""

    name = models.CharField(max_length=200)


class Pokemon(models.Model):
    """List the details of a given Pokemon."""

    name = models.CharField(max_length=200, unique=True)
    base_experience = models.IntegerField(default=None)
    height = models.IntegerField(default=None)
    weight = models.IntegerField(default=None)
    is_default = models.BooleanField(default=None)
    first_move = models.ForeignKey(Move, on_delete=models.CASCADE, default="")

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
