"""Summing the elements of a list suing different loops"""

__author__ = "730754347"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    sum: float = 0.0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for number in vals:
        sum += number
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for number in range(0, len(vals)):
        sum += number
    return sum
