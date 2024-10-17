"""Unit tests to test function."""

__author__ = "730754347"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_expected() -> None:
    a: list[int] = [1, 2, 5, 9, 2, 9]
    assert find_and_remove_max(a) == 9


def test_find_and_remove_max_mutate() -> None:
    a: list[int] = [1, 2, 5, 9, 2, 9]
    assert a == [1, 2, 5, 2]


def test_find_and_remove_max_edge() -> None:
    a: list[int] = [-2, -5, -3]
    assert find_and_remove_max(a) == -2


def test_find_and_remove_max_unconventional() -> None:
    a: list[int] = []
    assert find_and_remove_max(a) == -1
