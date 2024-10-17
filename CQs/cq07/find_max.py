"""Defining function."""

__author__ = "730754347"


def find_and_remove_max(a: list[int]) -> int:
    """Identifies max int in list and removes it"""
    if len(a) == 0:
        return -1
    index1: int = 0
    index2: int = 0
    largest: int = a[0]
    while index1 < len(a):
        if a[index1] > largest:
            largest = a[index1]
        index1 += 1
    while index2 < len(a):
        if a[index2] == largest:
            a.pop(index2)
        else:
            index2 += 1
    return largest
