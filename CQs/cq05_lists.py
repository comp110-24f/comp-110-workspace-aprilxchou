"""Mutating functions."""

__author__ = "730754347"


def manual_append(a: list[int], b: int) -> None:
    a.append(b)


def double(c: list[int]) -> None:
    index: int = 0
    while index < len(c):
        c[index] = 2 * c[index]
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
