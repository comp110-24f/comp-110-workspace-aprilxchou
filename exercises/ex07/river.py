"""File to define River class."""

__author__ = "730754347"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Creates new class of River."""

    day: int
    bear: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes old bears and fish."""
        alive_bears: list[Bear] = []
        for bear in range(0, len(self.bears)):
            if self.bears[bear].age <= 5:
                alive_bears.append(self.bears[bear])  # adds alive bears to new list
        alive_fish: list[Fish] = []
        for fish in range(0, len(self.fish)):
            if self.fish[fish].age <= 3:
                alive_fish.append(self.fish[fish])  # adds alive fish to new list
        self.bears = alive_bears
        self.fish = alive_fish
        return None

    def remove_fish(self, amount: int):
        """Removes amount of fish from list."""
        count: int = 0
        while count < amount:
            self.fish.pop(0)  # removes that amount of fish
            count += 1
        return None

    def bears_eating(self):
        """Removes eaten fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)  # remove 3 fish
                bear.eat(3)  # add hunger score of 3
        return None

    def check_hunger(self):
        """Checks if bear has starved."""
        alive_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                alive_bears.append(bear)  # only adds alive bears
        self.bears = alive_bears
        return None

    def repopulate_fish(self):
        """Models fish reproduction."""
        new_fish: int = (len(self.fish) // 2) * 4
        for pair_fish in range(0, new_fish):
            self.fish.append(Fish())  # adds new fish
        return None

    def repopulate_bears(self):
        """Models bear reproduction."""
        new_bears: int = len(self.bears) // 2
        for pair_bear in range(0, new_bears):
            self.bears.append(Bear())  # creates new bear for every two  bears
        return None

    def view_river(self):
        """Prints stats of river."""
        print(f"~~~ Day {self.day}: ~~~")  # how many days
        print(f"Fish population: {len(self.fish)}")  # number of fish
        print(f"Bear population: {len(self.bears)}")  # number of bears
        # prints how many days have passed, fish population, and bear population
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calls one_river_day 7 times."""
        day: int = 1
        while day <= 7:
            self.one_river_day()  # simulates one week
            day += 1
        return None
