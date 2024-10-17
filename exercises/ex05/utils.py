"""Implement list utility functions."""

__author__ = "730754347"


def only_evens(a: list[int]) -> list[int]:
    result: list[int] = []  # begin with empty list as default
    for number in a:  # use for to cycle through all elements
        if number % 2 == 0:  # use remainder function to test odd or even
            result.append(number)
    return result


def sub(b: list[int], start: int, end: int) -> list[int]:
    evens: list[int] = []
    if len(b) == 0:  # deal with edge cases first
        return evens
    if start >= len(b):
        return evens
    if end <= 0:
        return evens
    if start < 0:
        start = 0
    if end > len(b):
        end = len(b)  # change range so that function will work
    for index in range(start, end):
        evens.append(b[index])
    return evens


def add_at_index(e: list[int], integer: int, index: int) -> None:
    if index > len(e) or index < 0:  # will not work for these cases
        raise IndexError("Index is out of bounds for the input list")
    e.append(0)  # add the last element and an extra space
    for number in range(len(e) - 1, index, -1):  # will cause elements to go backwards
        e[number] = e[number - 1]  # replace with element before
    e[index] = integer  # end with final replacement
