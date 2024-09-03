"""Calculate supplies and cost for tea party"""

__author__: str = "730754347"


# remember to put string literals in quotes
def main_planner(guests: int) -> None:
    "Calls all functions and produces printed output"
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # very important to put str() before int or float values
    # be sure to assign values to variables in functions
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=2 * guests, treat_count=3 * guests)))
    # had to manipulate guests to come up with values for tea_count and treat_count


# when interacting, must type "tea_bags(people=_)" to call function
def tea_bags(people: int) -> int:
    """Return number of tea bags."""
    return people * 2


def treats(people: int) -> int:
    """Return number of treats."""
    return people * 3


def cost(tea_count: int, treat_count: int) -> float:
    """Return total cost of tea bags and treats"""
    return tea_count * 0.5 + treat_count * 0.75


# put after all other functions, NOT at the beginning so that all functions can be read
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
