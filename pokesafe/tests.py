"""Ensure that we write good code."""

from django.test import TestCase

from .models import Pokemon


class PokemonModelTests(TestCase):
    """Test the methods of a Pokemon object."""

    def test_greet_if_weight(self):
        test_name = "Bulbasor"
        test_weight = 69
        bulbasor = Pokemon(name=test_name, weight=test_weight)

        greeting = bulbasor.greet()
        self.assertEqual(
            greeting, f"Hi, my name is {test_name} and I weigh {test_weight}!"
        )

    def test_greet_if_no_weight(self):
        test_name = "Bulbasor"
        bulbasor = Pokemon(name=test_name)

        greeting = bulbasor.greet()
        self.assertEqual(greeting, f"Hi, my name is {test_name}!")
