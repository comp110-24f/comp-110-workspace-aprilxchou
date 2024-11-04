"""File to define Fish class."""

__author__ = "730754347"


class Fish:
    """Defines new class of Fish."""

    age: int

    def __init__(self):
        """Starting fish."""
        self.age = 0
        return None

    def one_day(self):
        """What happens every day for fish."""
        self.age += 1
        return None
