"""Write unit tests."""

__author__ = "730754347"

from exercises.ex05.utils import only_evens, sub, add_at_index

import pytest


def test_only_evens_edge() -> None:
    """Testing for empty list"""
    assert only_evens([]) == []  # returns nothing if no numbers


def test_only_evens_return() -> None:
    """Testing result for only evens"""
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]  # only even numbers


def test_only_evens_mutate() -> None:
    """Testing that function does not mutate original list"""
    a: list[int] = [1, 2, 3, 4, 5]
    only_evens(a)
    assert a == [1, 2, 3, 4, 5]  # list unchanged


def test_sub_edge() -> None:
    """Testing for start index out of range"""
    assert sub([1, 2, 3], 5, 6) == []  # return empty list


def test_sub_return() -> None:
    """Testing for correct sublist"""
    assert sub([2, 4, 6, 8], 0, 3) == [2, 4, 6]  # new sublist between range


def test_sub_mutate() -> None:
    """Testing that function does not mutate original list"""
    a: list[int] = [2, 4, 6, 8]
    sub(a, 0, 3)
    assert a == [2, 4, 6, 8]  # does not change


def test_add_at_index_indexerror():
    """Test that function raises IndexError for index out of range"""
    a: list[int] = [2, 3, 4]
    with pytest.raises(IndexError):
        add_at_index(a, 4, 9)  # index out of range


def test_add_at_index_case() -> None:
    """Testing that function adds element at index"""
    a: list[int] = [2, 3, 4]
    add_at_index(a, 5, 3)
    assert a == [2, 3, 3, 4]  # normal use


def test_add_at_index_mutate() -> None:
    """Testing that return is None"""
    a: list[int] = [2, 3, 4]
    assert add_at_index(a, 5, 3) is None  # must use is statement for None
