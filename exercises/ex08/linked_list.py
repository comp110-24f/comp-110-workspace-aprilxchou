"""Linked List Utils."""

from __future__ import annotations

__author__ = "730754347"


class Node:
    """A class representing a single node in a linked list."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None = None):
        """Initialize a Node with a given value and an optional next node."""
        # Assign the value to the node and link it to the next node, if provided.
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        # Base case: if this is the last node, represent as "value -> None".
        if self.next is None:
            return f"{self.value} -> None"
        # Recursive case: append "value -> " to the next node’s string representation.
        else:
            return f"{self.value} -> {self.next}"


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    # Base case: if there are no nodes, return "None".
    if head is None:
        return "None"
    # Recursive case: represent the current node and recurse on the next node.
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # Base case: if this is the last node, return its value.
    if head.next is None:
        return head.value
    # Recursive case: call last on the next node to keep going until the end.
    else:
        return last(head.next)


def value_at(head: Node | None, index: int) -> int:
    """Return the value at the given index in the linked list."""
    # If head is None, the index is out of bounds; raise an error.
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    # Base case: if index is 0, return the current node’s value.
    if index == 0:
        return head.value
    # Recursive case: move to the next node, reducing index by 1 each time.
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return the maximum value in the linked list."""
    # If head is None, list is empty; raise an error.
    if head is None:
        raise ValueError("Cannot call max_value with None")
    # Base case: if this is the last node, return its value as the max.
    if head.next is None:
        return head.value
    # Recursive case
    max_rest = max(head.next)
    return head.value if head.value > max_rest else max_rest


def linkify(items: list[int]) -> Node | None:
    """Convert a list of integers into a linked list."""
    # Base case: if the list is empty, return None (no nodes).
    if len(items) == 0:
        return None
    # Recursive case: create a node with the first item and link to the rest.
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Return a new linked list with all values scaled by the given factor."""
    # Base case: if head is None, return None (end of the new list).
    if head is None:
        return None
    # Recursive case: scale the current node’s value and continue scaling the rest.
    return Node(head.value * factor, scale(head.next, factor))
