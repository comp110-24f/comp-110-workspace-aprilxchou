"""Utility functions to modify lists."""

__author__ = "730754347"


def all(a: list[int], b: int) -> bool:
    """Returns whether or not all elements in list are the same as the int."""
    index: int = 0  # use index to evaluate each list at each index
    if len(a) == 0:
        return False
    while index < len(a):
        if a[index] == b:
            index += 1
        else:
            return False  # will return False if one mismatch
    return True  # all conditions must be satisfied, so put at end


def max(c: list[int]) -> int:
    """Returns max value in a list."""
    if len(c) == 0:
        raise ValueError("c is an empty List")  # put ValueError first to exit function
    index: int = 0
    greatest_value: int = c[0]  # use this variable to keep track of greatest int
    while index < len(c):
        if c[index] > greatest_value:
            greatest_value = c[
                index
            ]  # change greatest_value if there is a new greatest value
        index += 1
    return greatest_value


def is_equal(d: list[int], e: list[int]) -> bool:
    """Determines if two lists are identical."""
    index: int = 0
    if len(d) != len(e):  # automatically False if two lists are unequal length
        return False
    while index < len(d) and index < len(
        e
    ):  # don't know which list is longer or shorter
        if d[index] != e[index]:
            return False  # immediately False at one error
        index += 1
    return True  # must pass all indexes to be True


def extend(f: list[int], g: list[int]) -> None:
    """Adds second list of ints to the end of the first list."""
    index: int = 0
    while index < len(g):
        f.append(g[index])  # must add each value individually
        index += 1
