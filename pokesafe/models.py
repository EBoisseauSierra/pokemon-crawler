"""Define the data model of the app."""

from django.db import models


class Move(models.Model):
    """Represent a given 'move' of a Pokemon."""

    name = models.CharField(max_length=200)

    def __repr__(self):
        """Provide a human-readable representation of the object."""
        return f"<Move({self.name})>"


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

    def __repr__(self):
        """Provide a human-readable representation of the object."""
        args = [
            self.name,
            self.base_experience,
            self.height,
            self.weight,
            self.is_default,
            self.first_move,
        ]
        return f"<Pokemon({','.join(args)})>"
