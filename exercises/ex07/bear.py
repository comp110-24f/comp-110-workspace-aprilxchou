"""File to define Bear class."""

__author__ = "730754347"


class Bear:
    """Define class named Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Starting bear."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """What happens each day for bear."""
        self.age += 1
        self.hunger_score -= 1  # age and hunger increase every day
        return None

    def eat(self, num_fish: int):
        """Increases hunger score by number of fish eaten."""
        self.hunger_score += num_fish  # bear hunger score
        return None
